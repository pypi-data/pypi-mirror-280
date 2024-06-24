import sys
import cligenius
from rich.console import Console
from typing import Optional
from scalify.client.openai import AsyncScalifyClient
from scalify.types import StreamingChatResponse
from scalify.utilities.asyncio import run_sync
from scalify.utilities.openai import get_openai_client
from scalify.beta.assistants import Assistant
from scalify.cli.threads import threads_app
from scalify.cli.assistants import assistants_app, say as assistants_say

import platform

from cligenius import Context, Exit, echo

from scalify import __version__

app = cligenius.Cligenius(no_args_is_help=True)
console = Console()
app.add_cligenius(threads_app, name="thread")
app.add_cligenius(assistants_app, name="assistant")
app.command(name="say")(assistants_say)


@app.command()
def version(ctx: Context):
    if ctx.resilient_parsing:
        return
    echo(f"Version:\t\t{__version__}")
    echo(f"Python version:\t\t{platform.python_version()}")
    echo(f"OS/Arch:\t\t{platform.system().lower()}/{platform.machine().lower()}")
    raise Exit()


if __name__ == "__main__":
    app()
