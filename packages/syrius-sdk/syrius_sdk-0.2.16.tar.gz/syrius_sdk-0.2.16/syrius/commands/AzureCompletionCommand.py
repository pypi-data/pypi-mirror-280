from typing import Any

from syrius.commands.abstract import Command, AbstractCommand


class AzureCompletionCommand(Command):
    """ """
    id: int = 35
    messages: list[dict[str, Any]] | AbstractCommand
    api_key: str | AbstractCommand
    api_endpoint: str | AbstractCommand
    model: str | AbstractCommand
    temperature: float | AbstractCommand
    tools: dict[str, Any] | AbstractCommand
    extract: str | AbstractCommand
