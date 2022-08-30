from src.elements.base_element import BaseElement
from src.elements.constants import ElementType


class RectangleTextElement(BaseElement):
    def __init__(self, text: str, element_type: ElementType, is_multiple=False, x: int = 0, y: int = 0):
        super().__init__(x, y, element_type, is_multiple=is_multiple)
        self.width = 60
        self.height = 20
        self._text = text

    def render(self, canvas) -> None:
        canvas.create_rectangle(
            self.x, self.y, self.x + self.width, self.y + self.height,
            fill=self._get_fill_color(),
            outline='red' if self.is_active else 'black'
        )
        canvas.create_text(self.x + 30, self.y + 10, text=self._text)

    def is_point_in_element(self, x: int, y: int) -> bool:
        if (self.x <= x <= self.x + self.width) and (self.y <= y <= self.y + self.height):
            return True
        return False

    def _get_fill_color(self) -> str:
        if self.is_movable:
            return "green"
        return "orange"
