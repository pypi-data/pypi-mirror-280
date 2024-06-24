from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from docugenr8_core import Settings as CoreSettings


from collections.abc import Callable


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
