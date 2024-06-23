class Dto:
    def __init__(self) -> None:
        self.pages: list[DtoPage] = []
        self.fonts: list[DtoFont] = []
        # self.images: list[ImageData] = []


class DtoFont:
    def __init__(self, name: str, font_raw_data: bytes) -> None:
        self.name = name
        self.raw_data = font_raw_data


class DtoPage:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
        self.contents: list[object] = []


class DtoTextBox:
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None:
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._fill_color: None | tuple[int, int, int] = None
        self._line_color: None | tuple[int, int, int] = None
        self._line_width: float = 1.0
        self._line_pattern: tuple[int, int, int, int, int] = (0, 0, 0, 0, 0)
        self._text_area: None | DtoTextArea = None


class DtoTextArea:
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.height_empty_space: float = 0.0
        self.v_align: str = ""
        self.paragraphs: list[DtoParagraph] = []
        self.fragments: list[DtoFragment] = []


class DtoParagraph:
    def __init__(self, x: float, y: float, text_area: DtoTextArea) -> None:
        self.x = x
        self.y = y
        self.text_area = text_area
        self.width: float = 0.0
        self.height: float = 0.0
        self.h_align: str = ""
        self.chars: str = ""
        self.line_height_ratio: float = 0.0
        self.tab_size: float = 0.0
        self.first_line_indent: float = 0.0
        self.hanging_indent: float = 0.0
        self.left_indent: float = 0.0
        self.right_indent: float = 0.0
        self.space_before: float = 0.0
        self.space_after: float = 0.0
        self.num_of_lines: int = 0
        self.textlines: list[DtoTextLine] = []
        self.fragments: list[DtoFragment] = []


class DtoTextLine:
    def __init__(
        self,
        x: float,
        y: float,
        paragraph: DtoParagraph,
        justify_padding_after: float,
    ) -> None:
        self.x = x
        self.y = y
        self.paragraph = paragraph
        self.justify_padding_after = justify_padding_after
        self.width: float = 0.0
        self.height: float = 0.0
        self.baseline: float = 0.0
        self.space_after: float = 0.0
        self.paragraph_h_align: str = ""
        self.words: list[DtoWord] = []
        self.fragments: list[DtoFragment] = []


class DtoWord:
    def __init__(self, x: float, y: float, textline: DtoTextLine) -> None:
        self.x = x
        self.y = y
        self.textline = textline
        self.width: float = 0.0
        self.height: float = 0.0
        self.baseline: float = 0.0
        self.justify_space: float = 0.0
        self.fragments: list[DtoFragment] = []


class DtoFragment:
    def __init__(
        self,
        x: float,
        y: float,
        word: DtoWord,
    ) -> None:
        self.x = x
        self.y = y
        self.word = word
        self.width: float = 0.0
        self.height: float = 0.0
        self.baseline: float = 0.0
        self.chars: str = ""
        self.font_name: str = ""
        self.font_size: float = 0.0
        self.font_color: tuple[int, int, int] = (0, 0, 0)


class DtoBezier:
    def __init__(
        self,
        cp1_x: float,
        cp1_y: float,
        cp2_x: float,
        cp2_y: float,
        endp_x: float,
        endp_y: float,
    ) -> None:
        self._cp1_x = cp1_x
        self._cp1_y = cp1_y
        self._cp2_x = cp2_x
        self._cp2_y = cp2_y
        self._endp_x = endp_x
        self._endp_y = endp_y


class DtoPoint:
    def __init__(
        self,
        x: float,
        y: float,
    ) -> None:
        self._x = x
        self._y = y


class DtoCurve:
    def __init__(
        self,
        x: float,
        y: float,
        fill_color: tuple[int, int, int] | None = None,
        line_color: tuple[int, int, int] | None = (0, 0, 0),
        line_width: float = 1.0,
        line_pattern: tuple[int, int, int, int, int] = (0, 0, 0, 0, 0),
        closed: bool = False,
    ) -> None:
        self._fill_color = fill_color
        self._line_color = line_color
        self._line_width = line_width
        self._line_pattern = line_pattern
        self._closed = closed
        self._path: list[DtoPoint | DtoBezier] = [DtoPoint(x, y)]


class DtoRectangle:
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
        fill_color: tuple[int, int, int] | None,
        line_color: tuple[int, int, int] | None,
        line_width: float,
        line_pattern: tuple[int, int, int, int, int],
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotate = rotate
        self.skew = skew
        self.rounded_corner_top_left = rounded_corner_top_left
        self.rounded_corner_top_right = rounded_corner_top_right
        self.rounded_corner_bottom_left = rounded_corner_bottom_left
        self.rounded_corner_bottom_right = rounded_corner_bottom_right
        self.fill_color = fill_color
        self.line_color = line_color
        self.line_width = line_width
        self.line_pattern = line_pattern


class DtoArc:
    def __init__(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        line_color: tuple[int, int, int] | None,
        line_width: float,
        line_pattern: tuple[int, int, int, int, int],
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self._line_color = line_color
        self._line_width = line_width
        self._line_pattern = line_pattern


class DtoEllipse:
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        rotate: float,
        skew: float,
        fill_color: tuple[int, int, int] | None,
        line_color: tuple[int, int, int] | None,
        line_width: float,
        line_pattern: tuple[int, int, int, int, int],
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotate = rotate
        self.skew = skew
        self.fill_color = fill_color
        self.line_color = line_color
        self.line_width = line_width
        self.line_pattern = line_pattern
