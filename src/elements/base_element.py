import uuid
from abc import abstractmethod

from src.elements.constants import ElementType


class BaseElement:
    def __init__(self, x: int, y: int, element_type: ElementType, is_multiple: bool) -> None:
        self.x = x
        self.y = y
        self.id = str(uuid.uuid4())
        self.element_type = element_type
        self._is_active = False
        self.width = 0
        self.height = 0
        self.is_movable = False
        self._is_multiple = is_multiple

        self.child = None

    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value) -> None:
        if value != self._is_active:
            self._is_active = value

    @property
    def is_multiple(self) -> bool:
        return self._is_multiple

    @abstractmethod
    def render(self, canvas) -> None:
        pass

    @abstractmethod
    def is_point_in_element(self, x: int, y: int) -> bool:
        pass
