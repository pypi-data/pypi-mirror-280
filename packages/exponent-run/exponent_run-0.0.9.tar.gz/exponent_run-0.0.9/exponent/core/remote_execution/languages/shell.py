import asyncio
import os
import shlex
from asyncio.subprocess import Process

COMMAND_TIMEOUT = 30
TIMEOUT_MESSAGE = f"Command timed out after {COMMAND_TIMEOUT} seconds"


async def _read_stream(stream: asyncio.StreamReader | None) -> str | None:
    if stream is None:
        return None
    output = b""
    # Force the stream to not hang in case our command spawned
    # another long-running child process. We should only be
    # here if the parent command has an exit code, so this
    # should be safe... but we should revisit this later.
    stream.feed_eof()
    async for line in stream:
        output += line
    return output.decode("utf-8")


async def execute_shell(code: str, working_directory: str) -> str:
    shell_path = os.environ.get("SHELL", None)
    quoted_command = shlex.quote(code)

    full_command = quoted_command
    if shell_path:
        full_command = f"{shell_path} -i -c {quoted_command}"

    process: Process = await asyncio.create_subprocess_shell(
        full_command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=working_directory,
        start_new_session=True,
    )

    try:
        async with asyncio.timeout(COMMAND_TIMEOUT):
            while process.returncode is None:
                await asyncio.sleep(0.1)
    except TimeoutError:
        process.kill()
        return TIMEOUT_MESSAGE

    stdout_data = await _read_stream(process.stdout)
    stderr_data = await _read_stream(process.stderr)

    output = []
    if stdout_data:
        output.append(stdout_data)
    if stderr_data:
        output.append(stderr_data)
    shell_output = "\n".join(output)
    return shell_output
