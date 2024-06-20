from dataclasses import dataclass
from resemble.aio.types import GrpcMetadata
from resemble.settings import (
    MAX_BEARER_TOKEN_LENGTH,
    MAX_IDEMPOTENCY_KEY_LENGTH,
)
from typing import Optional


def validate_ascii(
    value: Optional[str],
    field_name: str,
    length_limit: int,
    *,
    illegal_characters: str = "",
    error_type: type[ValueError] = ValueError,
) -> None:
    if value is None:
        return
    if not isinstance(value, str):
        raise TypeError(
            f"The '{field_name}' option must be of type 'str', but got "
            f"'{type(value).__name__}'"
        )
    if len(value) > length_limit:
        raise error_type(
            f"The '{field_name}' option must be at most "
            f"{length_limit} characters long; the given value "
            f"is {len(value)} characters long"
        )
    if not value.isascii():
        raise error_type(
            f"The '{field_name}' option must be an ASCII string; the "
            f"given value '{value}' is not ASCII"
        )
    found = [c for c in value if c in illegal_characters]
    if len(found) > 0:
        raise error_type(
            f"The '{field_name}' option contained illegal characters: "
            f"{found!r}. The value was: {value!r}."
        )


@dataclass(kw_only=True, frozen=True)
class Options:
    """Options for RPCs."""
    idempotency_key: Optional[str] = None
    idempotency_alias: Optional[str] = None
    metadata: Optional[GrpcMetadata] = None
    bearer_token: Optional[str] = None

    def __post_init__(self):
        validate_ascii(
            self.idempotency_key,
            'idempotency_key',
            MAX_IDEMPOTENCY_KEY_LENGTH,
            error_type=InvalidIdempotencyKeyError,
            illegal_characters='\n',
        )
        validate_ascii(
            self.bearer_token,
            'bearer_token',
            MAX_BEARER_TOKEN_LENGTH,
            error_type=InvalidBearerTokenError,
            illegal_characters='\n',
        )

        if (
            self.idempotency_key is not None and
            self.idempotency_alias is not None
        ):
            raise TypeError(
                "options: only one of 'idempotency_key' or 'idempotency_alias' "
                "should be set"
            )


class InvalidActorIdError(ValueError):
    pass


class InvalidIdempotencyKeyError(ValueError):
    pass


class InvalidBearerTokenError(ValueError):
    pass


class MixedContextsError(ValueError):
    pass
