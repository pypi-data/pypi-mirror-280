from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from exponent.core.remote_execution.languages.python import Kernel


class RemoteExecutionClientSession:
    def __init__(self, working_directory: str):
        self.working_directory = working_directory
        self.kernel = Kernel(working_directory=working_directory)


@asynccontextmanager
async def get_session(
    working_directory: str,
) -> AsyncGenerator[RemoteExecutionClientSession, None]:
    session = RemoteExecutionClientSession(working_directory)
    try:
        yield session
    except Exception as e:
        session.kernel.close()
        raise e
