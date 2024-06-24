"""_summary_.

.
"""

from __future__ import annotations

from docugenr8_core import Document as CoreDocument
from docugenr8_core import Page as CorePage
from docugenr8_pdf import Pdf

from docugenr8.contents import Arc
from docugenr8.contents import Curve
from docugenr8.contents import Ellipse
from docugenr8.contents import Rectangle
from docugenr8.contents import TextArea
from docugenr8.contents import TextBox
from docugenr8.settings import Settings


class Document:
    """_summary_.

    .
    """

    def __init__(
        self,
        core_document: CoreDocument | None = None,
    ) -> None:
        """_summary_.

        .
        """
        if core_document is None:
            self.__core_document = CoreDocument()
        self.settings = Settings(self.__core_document.settings)
        self.pages: list[Page] = []
        self.doc_attributes: DocAttributes

    def add_font(
        self,
        font_name: str,
        path: str,
    ) -> None:
        self.__core_document.add_font(font_name, path)

    def add_page(
        self,
        width: float,
        height: float,
    ) -> None:
        page = Page(self.__core_document.add_page(width, height))
        self.pages.append(page)

    def create_textarea(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> TextArea:
        text_area = TextArea(x, y, width, height, self.__core_document)
        return text_area

    def create_textbox(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> TextBox:
        return TextBox(x, y, width, height, self.__core_document)

    def create_curve(self, x: float, y: float):
        return Curve(x, y, self.__core_document)

    def create_rectangle(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        rounded_corner_top_left: float = 0,
        rounded_corner_top_right: float = 0,
        rounded_corner_bottom_right: float = 0,
        rounded_corner_bottom_left: float = 0,
    ) -> Rectangle:
        return Rectangle(
            x,
            y,
            width,
            height,
            rounded_corner_top_left,
            rounded_corner_top_right,
            rounded_corner_bottom_right,
            rounded_corner_bottom_left,
            self.__core_document,
        )

    def create_arc(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
    ) -> Arc:
        return Arc(x1, y1, x2, y2, self.__core_document)

    def create_ellipse(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        rotate: float = 0,
        skew: float = 0,
    ) -> Ellipse:
        return Ellipse(x, y, width, height, self.__core_document)

    def output_to_bytes(
        self,
        file_format: str,
    ) -> bytes:
        match file_format:
            case "pdf":
                dto = self.__core_document.export("dto")
                return Pdf(dto).output_to_bytes()
            case _:
                raise NotImplementedError("Not supported file format.")

    def output_to_file(
        self,
        file_name: str,
        file_format: str = "pdf",
    ) -> None:
        b = self.output_to_bytes(file_format)
        with open(file_name, "wb") as f:
            f.write(b)


class Page:
    def __init__(
        self,
        core_page: CorePage,
    ) -> None:
        self.__core_page = core_page

    @property
    def width(self):
        return self.__core_page._width

    @width.setter
    def width(self, width: float):
        self.__core_page._width = width

    @property
    def height(self):
        return self.__core_page._height

    @height.setter
    def height(self, height: float):
        self.__core_page._height = height

    def add_content(
        self,
        content: object,
    ) -> None:
        if hasattr(content, "_get_core") and callable(getattr(content, "_get_core")):  # noqa: B009
            self.__core_page.add_content(content._get_core())  # type: ignore
        else:
            raise ValueError(f"The content {content.__class__.__name__} must have a _get_core() method.")


class DocAttributes:
    def __init__(
        self,
    ) -> None:
        pass
