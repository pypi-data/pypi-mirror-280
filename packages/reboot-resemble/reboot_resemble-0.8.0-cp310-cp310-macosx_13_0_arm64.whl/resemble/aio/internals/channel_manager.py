from __future__ import annotations

import asyncio
import grpc
import logging
from grpc.aio._base_channel import (
    StreamStreamMultiCallable,
    StreamUnaryMultiCallable,
    UnaryStreamMultiCallable,
    UnaryUnaryMultiCallable,
)
from grpc.aio._typing import DeserializingFunction, SerializingFunction
from resemble.aio.aborted import SystemAborted
from resemble.aio.resolvers import ActorResolver
from resemble.aio.types import (
    ActorId,
    RoutableAddress,
    ServiceName,
    StateTypeName,
    state_type_to_service,
)
from resemble.v1alpha1.errors_pb2 import UnknownService
from respect.logging import get_logger
from typing import Iterator, Optional

logger = get_logger(__name__)


class _ChannelManager:
    """Internal class for providing a grpc channel for a given service name and
    actor id.

    The channel manager is constructed and used internally and should never be
    created by the user.
    """
    _resolver: ActorResolver

    def __init__(self, resolver: ActorResolver, secure: bool):
        """
            resolver: gives addresses for each service/actor.
            secure: whether to use SSL when constructing channels.
        """
        self._resolver = resolver
        self._secure = secure

        # NOTE: As we cannot obtain the address from the `Channel` we store it
        # next to. This is needed to check if the channel has gone stale, e.g.,
        # if the address has changed. This would happen in local development as
        # the local envoy might restart on a new port.
        self._channels: dict[tuple[ServiceName, ActorId],
                             tuple[RoutableAddress, grpc.aio.Channel]] = {}

    def get_channel_from_state_type_name(
        self,
        state_type_name: StateTypeName,
        actor_id: ActorId,
        unresolvable_service_log_level: int = logging.ERROR,
    ) -> grpc.aio.Channel:
        return self.get_channel_from_service_name(
            state_type_to_service(state_type_name),
            actor_id,
            unresolvable_service_log_level=unresolvable_service_log_level
        )

    def get_channel_from_service_name(
        self,
        service_name: ServiceName,
        actor_id: ActorId,
        unresolvable_service_log_level: int = logging.ERROR,
    ) -> grpc.aio.Channel:
        """Returns a channel for the address provided by the resolver.

        If a channel for the given service name and actor id already exists,
        that channel will be returned. Otherwise, a new channel will be created
        and stored for future use.
        We additionally check that the address for the service has not changed.
        """

        key: tuple[ServiceName, ActorId] = (service_name, actor_id)
        address: Optional[RoutableAddress] = self._resolver.resolve_actor(
            service_name, actor_id
        )

        if address is None:
            logger.log(
                unresolvable_service_log_level,
                f"Failed to resolve service '{service_name}'; "
                "did you bring up a servicer for it in your `Application`?",
            )
            raise SystemAborted(UnknownService())

        if (
            key not in self._channels or self._channels[key][0] != address or
            self._channels[key][1].get_state()
            == grpc.ChannelConnectivity.SHUTDOWN
        ):
            # TODO: Do we want to pro-actively close the old channels here,
            # effectively cancelling all in-flight requests/streams, forcing a
            # reconnect with a new channel? We are not in an `async` context and
            # cannot call `await self._channels[key][1].close()` here.
            self._channels[key] = (address, self._create_channel(address))

        return self._channels[key][1]

    def channels(self) -> Iterator[grpc.aio.Channel]:
        """Returns all the channels that have been created by this channel
        manager."""
        return (channel for _, channel in self._channels.values())

    def _create_channel(
        self,
        address: RoutableAddress,
    ) -> grpc.aio.Channel:
        """Creates a channel for the address provided by the resolver."""
        if self._secure:
            return grpc.aio.secure_channel(
                address, grpc.ssl_channel_credentials()
            )

        return grpc.aio.insecure_channel(address)

    def get_channel_for(
        self,
        service_name: ServiceName,
        actor_id: ActorId,
    ) -> grpc.aio.Channel:
        """Syntactic sugar for 'get_channel_from_service_name()' that extracts
        the service name from a servicer type."""
        return self.get_channel_from_service_name(service_name, actor_id)


class LegacyGrpcChannel(grpc.aio.Channel):
    """An implementation of a `grpc.aio.Channel` that asks a `_ChannelManager` to
    give it a channel for every new service it is asked to connect to. It
    therefore wraps what may be many channels, or may be several copies of the
    same channel, picking the right one based on the service name.
    """

    def __init__(self, channel_manager: _ChannelManager):
        self._channel_manager = channel_manager
        self._borrowed_channels: dict[str, grpc.aio.Channel] = {}

    async def __aenter__(self) -> LegacyGrpcChannel:
        # We do not open any channels until we are asked about a particular
        # service.
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """When exiting our context, close all of the channels we ever
        opened."""
        await self.close()

    async def channel_ready(self) -> None:
        """A LegacyGrpcChannel is ready when all of its wrapped channels are
        ready.

        This method blocks until all the wrapped channels are ready.
        """
        await asyncio.gather(
            *[
                channel.channel_ready()
                for channel in self._borrowed_channels.values()
            ]
        )

    async def close(self, grace: Optional[float] = None) -> None:
        """Close all of the borrowed channels we ever opened."""
        await asyncio.gather(
            *[
                channel.close(grace)
                for channel in self._borrowed_channels.values()
            ]
        )

    def _get_channel_for_method(
        self, method_full_name: str
    ) -> grpc.aio.Channel:
        service_name = ServiceName(method_full_name.split('/')[1])
        return self._get_channel_for_service(service_name)

    def _get_channel_for_service(
        self, service_name: ServiceName
    ) -> grpc.aio.Channel:
        """Given a method name, get the channel for the service that that
        method is in, asking the _ChannelManager for it if we don't already know
        about it."""
        if service_name in self._borrowed_channels:
            return self._borrowed_channels[service_name]

        channel = self._channel_manager.get_channel_from_service_name(
            service_name,
            actor_id='',
        )
        self._borrowed_channels[service_name] = channel
        return channel

    def get_state(
        self, try_to_connect: bool = False
    ) -> grpc.ChannelConnectivity:
        # It's not clear how to implement this method when wrapping multiple
        # channels. Since this method is part of an experimental gRPC API, it's
        # OK for us to omit an implementation for the time being.
        raise NotImplementedError('Use alternative `get_state_for_service`')

    def get_state_for_service(
        self,
        # TODO(rjh): consider alternatives to `service_name` that can't be typo'd.
        service_name: ServiceName,
        try_to_connect: bool = False
    ) -> grpc.ChannelConnectivity:
        return self._get_channel_for_service(service_name
                                            ).get_state(try_to_connect)

    async def wait_for_state_change(
        self,
        last_observed_state: grpc.ChannelConnectivity,
    ) -> None:
        # It's not clear how to implement this method when wrapping multiple
        # channels. Since this method is part of an experimental gRPC API, it's
        # OK for us to omit an implementation for the time being.
        raise NotImplementedError(
            'Use alternative `wait_for_state_change_for_service`'
        )

    async def wait_for_state_change_for_service(
        self,
        # TODO(rjh): consider alternatives to `service_name` that can't be typo'd.
        service_name: ServiceName,
        last_observed_state: grpc.ChannelConnectivity,
    ) -> None:
        return self._get_channel_for_service(
            service_name
        ).wait_for_state_change(last_observed_state)

    def unary_unary(
        self,
        method: str,
        request_serializer: Optional[SerializingFunction] = None,
        response_deserializer: Optional[DeserializingFunction] = None
    ) -> UnaryUnaryMultiCallable:
        """See:
        https://grpc.github.io/grpc/python/grpc_asyncio.html#grpc.aio.Channel.unary_unary"""
        return self._get_channel_for_method(method).unary_unary(
            method, request_serializer, response_deserializer
        )

    def unary_stream(
        self,
        method: str,
        request_serializer: Optional[SerializingFunction] = None,
        response_deserializer: Optional[DeserializingFunction] = None
    ) -> UnaryStreamMultiCallable:
        """See:
        https://grpc.github.io/grpc/python/grpc_asyncio.html#grpc.aio.Channel.unary_stream"""
        return self._get_channel_for_method(method).unary_stream(
            method, request_serializer, response_deserializer
        )

    def stream_unary(
        self,
        method: str,
        request_serializer: Optional[SerializingFunction] = None,
        response_deserializer: Optional[DeserializingFunction] = None
    ) -> StreamUnaryMultiCallable:
        """See:
        https://grpc.github.io/grpc/python/grpc_asyncio.html#grpc.aio.Channel.stream_unary"""
        return self._get_channel_for_method(method).stream_unary(
            method, request_serializer, response_deserializer
        )

    def stream_stream(
        self,
        method: str,
        request_serializer: Optional[SerializingFunction] = None,
        response_deserializer: Optional[DeserializingFunction] = None
    ) -> StreamStreamMultiCallable:
        """See:
        https://grpc.github.io/grpc/python/grpc_asyncio.html#grpc.aio.Channel.stream_stream"""
        return self._get_channel_for_method(method).stream_stream(
            method, request_serializer, response_deserializer
        )
