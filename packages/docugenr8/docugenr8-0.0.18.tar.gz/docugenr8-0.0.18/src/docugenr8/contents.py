from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from docugenr8_core import Document as CoreDocument

from docugenr8_core.shapes import Arc as CoreArc
from docugenr8_core.shapes import Curve as CoreCurve
from docugenr8_core.shapes import Ellipse as CoreEllipse
from docugenr8_core.shapes import Rotation as CoreRotation
from docugenr8_core.shapes import Skew as CoreSkew
from docugenr8_core.shapes import Rectangle as CoreRectangle
from docugenr8_core.text_area import TextArea as CoreTextArea
from docugenr8_core.text_box import TextBox as CoreTextBox


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

    def add_rotation(
        self,
        x_origin: float,
        y_origin: float,
        degrees: float,
    ):
        self.__core_curve.transformations.append(CoreRotation(x_origin, y_origin, degrees))

    def add_skew(
        self,
        x_origin: float,
        y_origin: float,
        vertical_degrees: float,
        horizontal_degrees: float,
    ):
        self.__core_curve.transformations.append(CoreSkew(x_origin, y_origin, vertical_degrees, horizontal_degrees))


class Rectangle:
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
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
            rounded_corner_top_left,
            rounded_corner_top_right,
            rounded_corner_bottom_left,
            rounded_corner_bottom_right,
            core_document,
        )

    @property
    def rounded_corners_all(self) -> tuple[float, float, float, float]:
        result = (
            self.__core_rectangle.rounded_corner_top_left,
            self.__core_rectangle.rounded_corner_top_right,
            self.__core_rectangle.rounded_corner_bottom_right,
            self.__core_rectangle.rounded_corner_bottom_left,
        )
        return result

    @rounded_corners_all.setter
    def rounded_corners_all(self, value: float):
        self.__core_rectangle.rounded_corner_top_left = value
        self.__core_rectangle.rounded_corner_top_right = value
        self.__core_rectangle.rounded_corner_bottom_right = value
        self.__core_rectangle.rounded_corner_bottom_left = value

    @property
    def rounded_corner_top_left(self) -> float:
        return self.__core_rectangle.rounded_corner_top_left

    @rounded_corner_top_left.setter
    def rounded_corner_top_left(self, value: float):
        self.__core_rectangle.rounded_corner_top_left = value

    @property
    def rounded_corner_top_right(self) -> float:
        return self.__core_rectangle.rounded_corner_top_right

    @rounded_corner_top_right.setter
    def rounded_corner_top_right(self, value: float):
        self.__core_rectangle.rounded_corner_top_right = value

    @property
    def rounded_corner_bottom_right(self) -> float:
        return self.__core_rectangle.rounded_corner_bottom_right

    @rounded_corner_bottom_right.setter
    def rounded_corner_bottom_right(self, value: float):
        self.__core_rectangle.rounded_corner_bottom_right = value

    @property
    def rounded_corner_bottom_left(self) -> float:
        return self.__core_rectangle.rounded_corner_bottom_left

    @rounded_corner_bottom_left.setter
    def rounded_corner_bottom_left(self, value: float):
        self.__core_rectangle.rounded_corner_bottom_left = value

    def add_rotation(
        self,
        x_origin: float,
        y_origin: float,
        degrees: float,
    ):
        self.__core_rectangle.transformations.append(CoreRotation(x_origin, y_origin, degrees))

    def add_skew(
        self,
        x_origin: float,
        y_origin: float,
        vertical_degrees: float,
        horizontal_degrees: float,
    ):
        self.__core_rectangle.transformations.append(CoreSkew(x_origin, y_origin, vertical_degrees, horizontal_degrees))

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

    def add_rotation(
        self,
        x_origin: float,
        y_origin: float,
        degrees: float,
    ):
        self.__core_arc.transformations.append(CoreRotation(x_origin, y_origin, degrees))

    def add_skew(
        self,
        x_origin: float,
        y_origin: float,
        vertical_degrees: float,
        horizontal_degrees: float,
    ):
        self.__core_arc.transformations.append(CoreSkew(x_origin, y_origin, vertical_degrees, horizontal_degrees))

    def _get_core(self) -> CoreArc:
        return self.__core_arc


class Ellipse:
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        core_document: CoreDocument,
    ) -> None:
        self.__core_ellipse = CoreEllipse(x, y, width, height, core_document)

    def add_rotation(
        self,
        x_origin: float,
        y_origin: float,
        degrees: float,
    ):
        self.__core_ellipse.transformations.append(CoreRotation(x_origin, y_origin, degrees))

    def add_skew(
        self,
        x_origin: float,
        y_origin: float,
        vertical_degrees: float,
        horizontal_degrees: float,
    ):
        self.__core_ellipse.transformations.append(CoreSkew(x_origin, y_origin, vertical_degrees, horizontal_degrees))

    def _get_core(self) -> CoreEllipse:
        return self.__core_ellipse
