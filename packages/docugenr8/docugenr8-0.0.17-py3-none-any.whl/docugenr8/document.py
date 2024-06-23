"""_summary_.

.
"""

from __future__ import annotations

from collections.abc import Callable

from docugenr8_core import Document as CoreDocument
from docugenr8_core.page import Page as CorePage
from docugenr8_core.settings import Settings as CoreSettings
from docugenr8_core.shapes import Arc as CoreArc
from docugenr8_core.shapes import Curve as CoreCurve
from docugenr8_core.shapes import Rectangle as CoreRectangle
from docugenr8_core.shapes import Ellipse as CoreEllipse
from docugenr8_core.text_area import TextArea as CoreTextArea
from docugenr8_core.text_box import TextBox as CoreTextBox
from docugenr8_pdf.pdf import Pdf


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
        rotate: float = 0,
        skew: float = 0,
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
            rotate,
            skew,
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
        return Ellipse(x, y, width, height, rotate, skew, self.__core_document)

    def output_to_bytes(
        self,
        file_format: str,
    ) -> bytes:
        match file_format:
            case "pdf":
                dto = self.__core_document.build_dto()
                return Pdf(dto).output_to_bytes()
            case _:
                raise NotImplementedError("Not supported file format.")

    def output_to_file(
        self,
        file_format: str,
        file_name: str,
    ) -> None:
        match file_format:
            case "pdf":
                b = self.output_to_bytes(file_format)
                with open(file_name, "wb") as f:
                    f.write(b)
            case _:
                raise NotImplementedError("Not supported file format.")


class Settings:
    def __init__(
        self,
        core_settings: CoreSettings,
    ) -> None:
        self.__core_settings = core_settings

    @property
    def font_current(self):
        return self.__core_settings.font_current

    @font_current.setter
    def font_current(self, font_name: str):
        self.__core_settings.font_current = font_name

    @property
    def font_size(self):
        return self.__core_settings.font_size

    @font_size.setter
    def font_size(self, font_size: float):
        self.__core_settings.font_size = font_size

    @property
    def font_color(self):
        return self.__core_settings.font_color

    @font_color.setter
    def font_color(self, font_color: tuple[int, int, int]):
        self.__core_settings.font_color = font_color

    @property
    def text_tab_size(self):
        return self.__core_settings.text_tab_size

    @text_tab_size.setter
    def text_tab_size(self, tab_size: float):
        self.__core_settings.text_tab_size = tab_size

    @property
    def text_h_align(self):
        return self.__core_settings.text_h_align

    @text_h_align.setter
    def text_h_align(self, h_align: str):
        self.__core_settings.text_h_align = h_align

    @property
    def text_v_align(self):
        return self.__core_settings.text_v_align

    @text_v_align.setter
    def text_v_align(self, v_align: str):
        self.__core_settings.text_v_align = v_align

    @property
    def text_line_height_ratio(self):
        return self.__core_settings.textline_height_ratio

    @text_line_height_ratio.setter
    def text_line_height_ratio(self, height_ratio: float):
        self.__core_settings.textline_height_ratio = height_ratio

    @property
    def text_split_words(self):
        return self.__core_settings.text_split_words

    @text_split_words.setter
    def text_split_words(self, split_words: bool):
        self.__core_settings.text_split_words = split_words

    @property
    def paragraph_first_line_indent(self):
        return self.__core_settings.paragraph_first_line_indent

    @paragraph_first_line_indent.setter
    def paragraph_first_line_indent(self, indent: float):
        self.__core_settings.paragraph_first_line_indent = indent

    @property
    def paragraph_hanging_indent(self):
        return self.__core_settings.paragraph_hanging_indent

    @paragraph_hanging_indent.setter
    def paragraph_hanging_indent(self, indent: float):
        self.__core_settings.paragraph_hanging_indent = indent

    @property
    def paragraph_left_indent(self):
        return self.__core_settings.paragraph_left_indent

    @paragraph_left_indent.setter
    def paragraph_left_indent(self, indent: float):
        self.__core_settings.paragraph_left_indent = indent

    @property
    def paragraph_right_indent(self):
        return self.__core_settings.paragraph_right_indent

    @paragraph_right_indent.setter
    def paragraph_right_indent(self, indent: float):
        self.__core_settings.paragraph_right_indent = indent

    @property
    def paragraph_space_before(self):
        return self.__core_settings.paragraph_space_before

    @paragraph_space_before.setter
    def paragraph_space_before(self, space: float):
        self.__core_settings.paragraph_space_before = space

    @property
    def paragraph_space_after(self):
        return self.__core_settings.paragraph_space_after

    @paragraph_space_after.setter
    def paragraph_space_after(self, space: float):
        self.__core_settings.paragraph_space_after = space

    @property
    def page_num_current_page_dummy(self):
        return self.__core_settings.page_num_current_page_dummy

    @page_num_current_page_dummy.setter
    def page_num_current_page_dummy(self, page_dummy: str):
        self.__core_settings.page_num_current_page_dummy = page_dummy

    @property
    def page_num_total_pages_dummy(self):
        return self.__core_settings.page_num_total_pages_dummy

    @page_num_total_pages_dummy.setter
    def page_num_total_pages_dummy(self, page_dummy: str):
        self.__core_settings.page_num_total_pages_dummy = page_dummy

    @property
    def page_num_dummy_length(self):
        return self.__core_settings.page_num_dummy_length

    @page_num_dummy_length.setter
    def page_num_dummy_length(self, length: int):
        self.__core_settings.page_num_dummy_length = length

    @property
    def page_num_presentation(self):
        return self.__core_settings.page_num_presentation

    @page_num_presentation.setter
    def page_num_presentation(self, presentation: Callable[[int], str]):
        self.__core_settings.page_num_presentation = presentation

    # self.fill_color: tuple[int, int, int] = (255, 255, 255)  # white color 255, 255, 255
    @property
    def fill_color(self):
        return self.__core_settings.fill_color

    @fill_color.setter
    def fill_color(self, color: tuple[int, int, int]):
        self.__core_settings.fill_color = color

    # self.line_color: tuple[int, int, int] = (0, 0, 0)  # black color 0, 0, 0
    @property
    def line_color(self):
        return self.__core_settings.line_color

    @line_color.setter
    def line_color(self, color: tuple[int, int, int]):
        self.__core_settings.line_color = color

    # self.line_width: float = 1.0
    @property
    def line_width(self):
        return self.__core_settings.line_width

    @line_width.setter
    def line_width(self, width: float):
        self.__core_settings.line_width = width

    # self.line_pattern: tuple[int, int, int, int, int] = (0, 0, 0, 0, 0)
    @property
    def line_pattern(self):
        return self.__core_settings.line_pattern

    @line_pattern.setter
    def line_pattern(self, pattern: tuple[int, int, int, int, int]):
        self.__core_settings.line_pattern = pattern

    # self.textbox_padding_left: float = 0.0
    @property
    def textbox_padding_left(self):
        return self.__core_settings.textbox_padding_left

    @textbox_padding_left.setter
    def textbox_padding_left(self, padding: float):
        self.__core_settings.textbox_padding_left = padding

    # self.textbox_padding_right: float = 0.0
    @property
    def textbox_padding_right(self):
        return self.__core_settings.textbox_padding_right

    @textbox_padding_right.setter
    def textbox_padding_right(self, padding: float):
        self.__core_settings.textbox_padding_right = padding

    # self.textbox_padding_top: float = 0.0
    @property
    def textbox_padding_top(self):
        return self.__core_settings.textbox_padding_top

    @textbox_padding_top.setter
    def textbox_padding_top(self, padding: float):
        self.__core_settings.textbox_padding_top = padding

    # self.textbox_padding_bottom: float = 0.0
    @property
    def textbox_padding_bottom(self):
        return self.__core_settings.textbox_padding_bottom

    @textbox_padding_bottom.setter
    def textbox_padding_bottom(self, padding: float):
        self.__core_settings.textbox_padding_bottom = padding

    # self.textbox_margin_left: float = 0.0
    @property
    def textbox_margin_left(self):
        return self.__core_settings.textbox_margin_left

    @textbox_margin_left.setter
    def textbox_margin_left(self, margin: float):
        self.__core_settings.textbox_margin_left = margin

    # self.textbox_margin_right: float = 0.0
    @property
    def textbox_margin_right(self):
        return self.__core_settings.textbox_margin_right

    @textbox_margin_right.setter
    def textbox_margin_right(self, margin: float):
        self.__core_settings.textbox_margin_right = margin

    # self.textbox_margin_top: float = 0.0
    @property
    def textbox_margin_top(self):
        return self.__core_settings.textbox_margin_top

    @textbox_margin_top.setter
    def textbox_margin_top(self, margin: float):
        self.__core_settings.textbox_margin_top = margin

    # self.textbox_margin_bottom: float = 0.0
    @property
    def textbox_margin_bottom(self):
        return self.__core_settings.textbox_margin_bottom

    @textbox_margin_bottom.setter
    def textbox_margin_bottom(self, margin: float):
        self.__core_settings.textbox_margin_bottom = margin

    @property
    def line_closed(self):
        return self.__core_settings.line_closed

    @line_closed.setter
    def line_closed(self, value: bool):
        self.__core_settings.line_closed = value


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
        match content:
            case TextArea():
                self.__core_page.add_content(content._get_core())
            case TextBox():
                self.__core_page.add_content(content._get_core())
            case Curve():
                self.__core_page.add_content(content._get_core())
            case Rectangle():
                self.__core_page.add_content(content._get_core())
            case Arc():
                self.__core_page.add_content(content._get_core())
            case Ellipse():
                self.__core_page.add_content(content._get_core())
            case _:
                raise ValueError("Type not defined in main module.")


class DocAttributes:
    def __init__(
        self,
    ) -> None:
        pass


class TextArea:
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        core_document: CoreDocument,
    ) -> None:
        self.__core_text_area = core_document.create_textarea(x, y, width, height)

    def _get_core(self) -> CoreTextArea:
        return self.__core_text_area

    def add_text(
        self,
        unicode_text: str,
    ) -> None:
        self.__core_text_area.add_text(unicode_text)

    def link_textarea(
        self,
        next_textarea: TextArea,
    ) -> None:
        self.__core_text_area.link_textarea(next_textarea.__core_text_area)

    def set_width(
        self,
        new_width: float,
    ) -> None:
        self.__core_text_area.set_width(new_width)


class TextBox:
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        core_document: CoreDocument,
    ) -> None:
        self.__core_text_box = core_document.create_textbox(x, y, width, height)

    def add_text(self, unicode_text: str) -> None:
        self.__core_text_box.add_text(unicode_text)

    def _get_core(self) -> CoreTextBox:
        return self.__core_text_box


class Curve:
    def __init__(self, x: float, y: float, core_document: CoreDocument) -> None:
        self.__core_curve = core_document.create_curve(x, y)

    def _get_core(self) -> CoreCurve:
        return self.__core_curve

    def add_point(
        self,
        x: float,
        y: float,
    ) -> None:
        self.__core_curve.add_point(x, y)

    def add_bezier(
        self,
        cp1_x: float,
        cp1_y: float,
        cp2_x: float,
        cp2_y: float,
        endp_x: float,
        endp_y: float,
    ) -> None:
        self.__core_curve.add_bezier(cp1_x, cp1_y, cp2_x, cp2_y, endp_x, endp_y)


class Rectangle:
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        rotate: float,
        skew: float,
        rounded_corner_top_left: float,
        rounded_corner_top_right: float,
        rounded_corner_bottom_left: float,
        rounded_corner_bottom_right: float,
        core_document: CoreDocument,
    ) -> None:
        self.__core_rectangle = CoreRectangle(
            x,
            y,
            width,
            height,
            rotate,
            skew,
            rounded_corner_top_left,
            rounded_corner_top_right,
            rounded_corner_bottom_left,
            rounded_corner_bottom_right,
            core_document,
        )

    @property
    def rounded_corners_all(self) -> tuple[float, float, float, float]:
        result = (
            self.__core_rectangle._dto_rectangle.rounded_corner_top_left,
            self.__core_rectangle._dto_rectangle.rounded_corner_top_right,
            self.__core_rectangle._dto_rectangle.rounded_corner_bottom_right,
            self.__core_rectangle._dto_rectangle.rounded_corner_bottom_left,
        )
        return result

    @rounded_corners_all.setter
    def rounded_corners_all(self, value: float):
        self.__core_rectangle._dto_rectangle.rounded_corner_top_left = value
        self.__core_rectangle._dto_rectangle.rounded_corner_top_right = value
        self.__core_rectangle._dto_rectangle.rounded_corner_bottom_right = value
        self.__core_rectangle._dto_rectangle.rounded_corner_bottom_left = value

    @property
    def rounded_corner_top_left(self) -> float:
        return self.__core_rectangle._dto_rectangle.rounded_corner_top_left

    @rounded_corner_top_left.setter
    def rounded_corner_top_left(self, value: float):
        self.__core_rectangle._dto_rectangle.rounded_corner_top_left = value

    @property
    def rounded_corner_top_right(self) -> float:
        return self.__core_rectangle._dto_rectangle.rounded_corner_top_right

    @rounded_corner_top_right.setter
    def rounded_corner_top_right(self, value: float):
        self.__core_rectangle._dto_rectangle.rounded_corner_top_right = value

    @property
    def rounded_corner_bottom_right(self) -> float:
        return self.__core_rectangle._dto_rectangle.rounded_corner_bottom_right

    @rounded_corner_bottom_right.setter
    def rounded_corner_bottom_right(self, value: float):
        self.__core_rectangle._dto_rectangle.rounded_corner_bottom_right = value

    @property
    def rounded_corner_bottom_left(self) -> float:
        return self.__core_rectangle._dto_rectangle.rounded_corner_bottom_left

    @rounded_corner_bottom_left.setter
    def rounded_corner_bottom_left(self, value: float):
        self.__core_rectangle._dto_rectangle.rounded_corner_bottom_left = value

    def _get_core(self) -> CoreRectangle:
        return self.__core_rectangle


class Arc:
    def __init__(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        core_document: CoreDocument,
    ) -> None:
        self.__core_arc = CoreArc(x1, y1, x2, y2, core_document)

    def _get_core(self) -> CoreArc:
        return self.__core_arc


class Ellipse:
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        rotate: float,
        skew: float,
        core_document: CoreDocument,
    ) -> None:
        self.__core_ellipse = CoreEllipse(x, y, width, height, rotate, skew, core_document)

    def _get_core(self) -> CoreEllipse:
        return self.__core_ellipse
