from __future__ import annotations

import urllib.parse
from contextlib import contextmanager
from io import BytesIO
from pathlib import Path
from typing import IO, Any, Callable, Iterator

import html5lib
import requests
from pydantic import BaseModel, Field, ValidationError
from xhtml2pdf import pisa

BASEURL = "https://www.enargus.de/pub/bscw.cgi/REST"


class EnArgusError(Exception):
    pass


def fetch(query: str) -> requests.Response:
    url = f"{BASEURL}/{query}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.HTTPError as err:
        msg = f"Error fetching from '{url}': {err}"
        raise EnArgusError(msg) from err
    return response


def _recursive_retrieve_text(nodes: Any) -> str:
    buf = []
    for node in nodes:
        if node.nodeType == node.TEXT_NODE:
            buf.append(node.data)
        else:
            buf.append(_recursive_retrieve_text(node.childNodes))
    return "".join(buf)


class Page(BaseModel):
    oid: int
    name: str
    translations: dict[str, Page] = Field(alias="langinfo", default_factory=dict)
    html: str = Field(repr=False, default_factory=str)

    @staticmethod
    def _fetch_and_parse(url: str) -> Page:
        response = fetch(url)
        try:
            return Page.model_validate(response.json())
        except ValidationError as err:
            msg = "Could not parse the response. Usually, this means the page does not exist."
            raise EnArgusError(msg) from err

    @staticmethod
    def fetch_from_oid(oid: int) -> Page:
        query = f"enargus.page?mode=1&page={oid}"
        return Page._fetch_and_parse(query)

    @staticmethod
    def fetch_from_query(name: str, lang: str) -> Page:
        name = urllib.parse.quote(name)
        query = f"enargus.page?mode=1&lang={lang.lower()}&page={name}"
        return Page._fetch_and_parse(query)

    def translate_to(self, lang: str) -> Page:
        if lang.lower() not in self.translations:
            raise EnArgusError(f"Translation to '{lang}' not available.")
        return self.translations[lang.lower()]

    def synchronize(self) -> None:
        new = Page.fetch_from_oid(self.oid)
        self.__dict__.update(new.__dict__)

    @property
    def content(self) -> str:
        parser = html5lib.HTMLParser(tree=html5lib.getTreeBuilder("dom"))
        dom = parser.parse(self.html)
        raw = _recursive_retrieve_text(dom.getElementsByTagName("body"))
        raw_split = raw.split("\n")
        lines = [line.lstrip().rstrip() for line in raw_split[1:]]  # First is title
        return "\n".join(lines)

    @property
    def lang(self) -> str:
        if not self.translations:
            self.synchronize()
        for lang, page in self.translations.items():
            if page.oid == self.oid:
                return lang
        raise EnArgusError("Could not determine language of the page. Please report.")

    def to_pdf(self) -> BytesIO:
        if not self.html:
            self.synchronize()

        buf = BytesIO()
        pisa_status = pisa.CreatePDF(self.html, dest=buf)

        if pisa_status.err:
            raise EnArgusError(f"Error converting HTML to PDF: {pisa_status.err}")

        return buf

    def to_json(self) -> str:
        return self.model_dump_json()


class PageCollection(BaseModel):
    lang: str
    pages: list[Page]

    def update_all(
        self, missing_only: bool = False, callback: Callable[..., None] | None = None
    ) -> None:
        if missing_only:
            to_be_updated = [page for page in self.pages if not page.html]
        else:
            to_be_updated = self.pages

        for page in to_be_updated:
            page.synchronize()
            if callback is not None:
                callback()

    def to_json(self) -> str:
        return self.model_dump_json()

    @staticmethod
    def get_all(lang: str) -> PageCollection:
        url = f"enargus.pagelist?lang={lang.lower()}"
        response = fetch(url)
        try:
            return PageCollection.model_validate(
                {"lang": lang, "pages": response.json()}
            )
        except ValidationError as err:
            msg = "Could not parse the response. Please report."
            raise EnArgusError(msg) from err

    @staticmethod
    def get_from_search(lang: str, query: str) -> PageCollection:
        url = f"enargus.search?lang={lang.lower()}&query={query}&only=wiki"
        response = fetch(url)
        try:
            return PageCollection.model_validate(
                {"lang": lang, "pages": response.json()["wiki"]}
            )
        except (ValidationError, KeyError) as err:
            msg = "Could not parse the response. Please report."
            raise EnArgusError(msg) from err

    @staticmethod
    def from_file(file: Path) -> PageCollection:
        with save_open(file, "r") as f:
            try:
                return PageCollection.model_validate_json(f.read())
            except ValidationError as err:
                msg = "Could not parse the file. Check for valid structure of JSON."
                raise EnArgusError(msg) from err


@contextmanager
def save_open(file: Path, mode: str) -> Iterator[IO[Any]]:
    try:
        with file.open(mode) as f:
            yield f
    except OSError as err:
        msg = f"Could not open file '{file}' with mode '{mode}': {err}"
        raise EnArgusError(msg) from err
