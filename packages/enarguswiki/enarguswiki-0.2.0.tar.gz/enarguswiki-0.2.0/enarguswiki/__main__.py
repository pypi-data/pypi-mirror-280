from contextlib import contextmanager
from enum import Enum
from io import StringIO
from pathlib import Path
from typing import Annotated, Any, Iterator, Optional

import typer
from rich import print as rprint
from rich.console import Console
from rich.progress import Progress
from rich.table import Table
from slugify import slugify

from enarguswiki import __version__
from enarguswiki.core import EnArgusError, Page, PageCollection

app = typer.Typer(no_args_is_help=True, pretty_exceptions_enable=False)


def version_callback(value: bool) -> None:
    if value:
        rprint(f"EnArgusWiki {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    _: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Print the version and exit",
    ),
) -> None:
    """CLI for the EnArgus wiki."""


class FileFormat(str, Enum):
    SUMMARY = "summary"
    JSON = "json"
    PDF = "pdf"


class Lang(str, Enum):
    DE = "DE"
    EN = "EN"
    ES = "ES"
    FR = "FR"
    PT = "PT"
    IT = "IT"


def save_to_file(name: str, path: Path, val: Any, suffix: str, mode: str = "w") -> None:
    if path.is_dir():
        name = slugify(name, max_length=80, word_boundary=True)
        path = path / f"{name}{suffix}"
        with open(path, mode) as f:
            f.write(val)
    else:
        path = path_with_correct_suffix(path, suffix)
        with open(path, mode) as f:
            f.write(val)


def path_with_correct_suffix(path: Path, suffix: str) -> Path:
    if path.suffix != suffix:
        new = path.with_suffix(suffix)
        msg = (
            "[bold red]WARNING:[/bold red] "
            f"Renaming the file with correct suffix ({path.name} -> {new.name})"
        )
        rprint(msg)
        return new
    return path


def summarize_page(page: Page) -> Table:
    table = Table(show_header=False, show_lines=True)
    table.add_column(justify="right", style="cyan", no_wrap=True)
    table.add_column()
    table.add_row("Object ID:", str(page.oid))
    table.add_row("Language:", page.lang)
    table.add_row("Name:", page.name)
    table.add_row("Content:", page.content)
    return table


@contextmanager
def catch_enargus_error() -> Iterator[None]:
    try:
        yield
    except EnArgusError as err:
        msg = f"[bold red]ERROR:[/bold red] {err}"
        rprint(msg)
        typer.Exit(1)


@app.command()
def page(
    oid: Annotated[
        Optional[int],
        typer.Option(help="The object ID of the page"),
    ] = None,
    query: Annotated[
        Optional[str],
        typer.Option(
            help="The query to search for.",
        ),
    ] = None,
    language: Annotated[
        Lang,
        typer.Option(
            help="Which language to use.",
        ),
    ] = Lang.DE,
    format: Annotated[
        FileFormat,
        typer.Option(
            help="Which format to output the page in.",
        ),
    ] = FileFormat.SUMMARY,
    out: Annotated[
        Optional[Path],
        typer.Option(
            help=(
                "Path to save the output. "
                "If it's a file, the file will be used. "
                "If it's a directory, the name of the page will be used as file name. "
                "If not provided, it will be printed to stdout."
            )
        ),
    ] = None,
) -> None:
    """Fetch a page from the EnArgus wiki."""
    with catch_enargus_error():
        oid_mode = (query is None) and (oid is not None)
        query_mode = (query is not None) and (oid is None)
        if not (oid_mode or query_mode):
            raise EnArgusError("Exactly one of 'oid' or 'query' must be provided.")

        if oid is not None:
            page = Page.fetch_from_oid(oid)

        elif query is not None:
            page = Page.fetch_from_query(query, language)

        match format:
            case FileFormat.SUMMARY:
                summary = summarize_page(page)
                if out is None:
                    rprint(summary)
                else:
                    console = Console(file=StringIO(), width=120)
                    console.print(summary)
                    save_to_file(page.name, out, console.file.getvalue(), ".txt")

            case FileFormat.JSON:
                json_data = page.to_json()
                if out is None:
                    typer.echo(json_data)
                else:
                    save_to_file(page.name, out, json_data, ".json")

            case FileFormat.PDF:
                pdf_data = page.to_pdf()
                if out is None:
                    typer.echo(pdf_data.getvalue())
                else:
                    save_to_file(page.name, out, pdf_data.getvalue(), ".pdf", mode="wb")


class CallbackProgressBar:
    def __init__(self, total: int, description: str) -> None:
        self._progress = Progress()
        self._task = self._progress.add_task(description, total=total, start=False)

    @contextmanager
    def contextmanager(self) -> Iterator[None]:
        self._progress.start()
        self._progress.start_task(self._task)
        yield
        self._progress.stop_task(self._task)
        self._progress.stop()

    def callback(self) -> None:
        self._progress.advance(self._task)


class UpdateMode(str, Enum):
    NONE_ = "none"
    ALL = "all"
    MISSING = "missing-only"


@app.command()
def collection(
    language: Annotated[
        Lang,
        typer.Option(
            help="Which language to use.",
        ),
    ] = Lang.DE,
    outp: Annotated[
        Optional[Path],
        typer.Option(
            "--out",
            help=(
                "Path to save the output. "
                "If it's a file, the file will be used. "
                "If it's a directory, then 'col-<LANGUAGE>.json' will be used. "
                "If not provided, it will be printed to stdout."
            ),
        ),
    ] = None,
    inp: Annotated[
        Optional[Path],
        typer.Option("--in", help="Path to load a collection from."),
    ] = None,
    update: Annotated[
        UpdateMode,
        typer.Option(
            help=(
                "How to update the pages. "
                "none: Do not update any pages. "
                "all: Update all pages no matter if there is content. "
                "missing-only: Update only the pages that have no content."
            ),
        ),
    ] = UpdateMode.NONE_,
) -> None:
    """Fetch a collection of pages from the EnArgus wiki."""
    with catch_enargus_error():
        if inp is not None:
            col = PageCollection.from_file(inp)
        else:
            col = PageCollection.get_all(language)

        if update in (UpdateMode.ALL, UpdateMode.MISSING):
            missing_only = update == UpdateMode.MISSING
            pb = CallbackProgressBar(len(col.pages), "Updating pages... ")
            with pb.contextmanager():
                col.update_all(callback=pb.callback, missing_only=missing_only)

        json_data = col.to_json()

        if outp is None:
            typer.echo(json_data)
        else:
            save_to_file(f"col-{language}", outp, json_data, ".json")


@app.command()
def search(
    query: Annotated[
        str,
        typer.Argument(help="The query to search for."),
    ],
    language: Annotated[
        Lang,
        typer.Option(
            help="Which language to use.",
        ),
    ] = Lang.DE,
) -> None:
    """Search for a query in the EnArgus wiki."""
    with catch_enargus_error():
        col = PageCollection.get_from_search(language, query)
        table = Table(
            title=f"[bold]Search results for '{query}' in {language.upper()}[/bold]\n"
        )
        table.add_column("ObjectID", justify="right", style="cyan", no_wrap=True)
        table.add_column(f"Name ({language.upper()})")

        for page in col.pages:
            name = page.name
            name = name.replace(
                query.capitalize(), f"[magenta]{query.capitalize()}[/magenta]"
            )
            name = name.replace(query.lower(), f"[magenta]{query.lower()}[/magenta]")

            table.add_row(str(page.oid), name)

        rprint(table)


@app.command()
def translate(
    oid: Annotated[
        int,
        typer.Option(help="The object ID of the page"),
    ],
    language: Annotated[
        Lang,
        typer.Option(
            help="Which language to translate to.",
        ),
    ] = Lang.DE,
) -> None:
    """Get a translated verison from the EnArgus wiki."""
    with catch_enargus_error():
        old = Page.fetch_from_oid(oid)
        new = old.translate_to(language)
        rprint(f"[bold]Translation from ({old.lang}) to ({new.lang})[/bold]\n")
        rprint(summarize_page(new))


if __name__ == "__main__":
    app()
