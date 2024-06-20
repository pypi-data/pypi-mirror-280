import aiofiles.os
import os
import sys
from resemble.cli import terminal
from resemble.cli.dev import (
    add_application_options,
    check_docker_status,
    try_and_become_child_subreaper_on_linux,
)
from resemble.cli.directories import (
    add_working_directory_options,
    use_working_directory,
)
from resemble.cli.rc import ArgumentParser
from resemble.cli.subprocesses import Subprocesses
from resemble.settings import (
    ENVVAR_LOCAL_ENVOY_TLS_CERTIFICATE_PATH,
    ENVVAR_LOCAL_ENVOY_TLS_KEY_PATH,
    ENVVAR_RSM_DIRECTORY,
    ENVVAR_RSM_EFFECT_VALIDATION,
    ENVVAR_RSM_LOCAL_ENVOY,
    ENVVAR_RSM_LOCAL_ENVOY_PORT,
    ENVVAR_RSM_NAME,
    ENVVAR_RSM_SECRETS_DIRECTORY,
    ENVVAR_RSM_SERVE,
)


def register_serve(parser: ArgumentParser):
    add_working_directory_options(parser.subcommand('serve'))

    add_application_options(parser.subcommand('serve'))

    parser.subcommand('serve').add_argument(
        '--directory',
        type=str,
        help='path to directory for durably storing application state',
        required=True,
    )

    parser.subcommand('serve').add_argument(
        '--name',
        type=str,
        help="name of application, used to differentiate within '--directory'",
        required=True,
    )

    parser.subcommand('serve').add_argument(
        '--port',
        type=int,
        help='port to listen on',
        required=True,
    )

    parser.subcommand('serve').add_argument(
        '--tls-certificate',
        type=str,
        help='path to TLS certificate to use',
        required=True,
    )

    parser.subcommand('serve').add_argument(
        '--tls-key',
        type=str,
        help='path to TLS key to use',
        required=True,
    )


async def serve(
    args,
    parser: ArgumentParser,
) -> int:
    """Invokes `serve` with the arguments passed to 'rsm serve'."""

    # Determine the working directory and move into it.
    with use_working_directory(args, parser, verbose=True):

        # If on Linux try and become a child subreaper so that we can
        # properly clean up all processes descendant from us!
        try_and_become_child_subreaper_on_linux()

        # Use `Subprocesses` to manage all of our subprocesses for us.
        subprocesses = Subprocesses()

        application = os.path.abspath(args.application)

        # TODO: run `rsm protoc` once.

        # Set all the environment variables that
        # 'resemble.aio.Application' will be looking for.
        #
        # We make a copy of the environment so that we don't change
        # our environment variables which might cause an issue.
        env = os.environ.copy()

        env[ENVVAR_RSM_SERVE] = 'true'

        assert args.name is not None

        env[ENVVAR_RSM_NAME] = args.name

        env[ENVVAR_RSM_DIRECTORY] = args.directory

        if args.secrets_directory is not None:
            env[ENVVAR_RSM_SECRETS_DIRECTORY] = args.secrets_directory

        # Check if Docker is running and can access the Envoy proxy image.
        # Fail otherwise.
        await check_docker_status(subprocesses)

        env[ENVVAR_RSM_LOCAL_ENVOY] = 'true'

        env[ENVVAR_RSM_LOCAL_ENVOY_PORT] = str(args.port)

        # Check that the TLS certificate and key they gave us are
        # valid files and set the `LocalEnvoy` environment variables.
        if not await aiofiles.os.path.isfile(args.tls_certificate):
            terminal.fail(
                f"Expecting file at --tls-certificate={args.tls_certificate}"
            )

        if not await aiofiles.os.path.isfile(args.tls_key):
            terminal.fail(f"Expecting file at --tls-key={args.tls_key}")

        env[ENVVAR_LOCAL_ENVOY_TLS_CERTIFICATE_PATH] = args.tls_certificate
        env[ENVVAR_LOCAL_ENVOY_TLS_KEY_PATH] = args.tls_key

        env[ENVVAR_RSM_EFFECT_VALIDATION] = 'DISABLED'

        # Also include all environment variables from '--env='.
        for (key, value) in args.env or []:
            env[key] = value

        if not await aiofiles.os.path.isfile(application):
            terminal.fail(f"Missing application at '{application}'")

        # Expect an executable if we haven't been asked to use
        # `python`.
        if (
            args.python is None and
            not await aiofiles.os.access(application, os.X_OK)
        ):
            terminal.fail(
                f"Expecting executable application at '{application}'. "
                "Specify '--python' if you want to run a Python application."
            )

        launcher = sys.executable if args.python is not None else None

        args = [application] if launcher is None else [launcher, application]

        async with subprocesses.exec(*args, env=env) as process:
            return await process.wait()
