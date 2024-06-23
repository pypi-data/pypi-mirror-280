__all__ = ["cli"]

import platform

import click

from word_ending_finder import __title__, __version__
from word_ending_finder.wef import WordEnding


@click.command(name="version")
def version() -> None:
    """Show current version"""
    ver_msg = f"{__title__} v{__version__}"
    click.echo(
        f"{ver_msg}\n"
        f"- os/type: {platform.system().lower()}\n"
        f"- os/kernel: {platform.version()}\n"
        f"- os/arch: {platform.machine().lower()}\n"
        f"- python version: {platform.python_version()}\n"
    )


@click.command(name="find")
@click.argument("word_ending", type=str)
@click.option(
    "--no-exact",
    "-e",
    "exact",
    is_flag=True,
    help="Exact match",
)
def find(word_ending: str, exact: bool) -> None:
    """Find words"""
    instance = WordEnding()
    temp = not exact
    out = instance.get_words(word_ending, temp)
    print(out)


@click.group(name="cli")
def cli() -> None:
    """vocr's command line interface"""
    pass


cli.add_command(version)
cli.add_command(find)
