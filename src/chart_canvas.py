import logging
from copy import deepcopy
from tkinter import Tk, Canvas, Menu, messagebox
from typing import List, Optional

from src.elements.base_element import BaseElement
from src.utils import detect_element_collision

logger = logging.getLogger(__name__)


class ChartCanvas:
    def __init__(self, master: Tk) -> None:
        self._master = master

        self._width = 395
        self._height = 598

        self._is_need_render_grid = False

        self._elements: List[BaseElement] = []

        self._selected_element: Optional[BaseElement] = None
        self._movable_element: Optional[BaseElement] = None
        self._is_move_action: bool = False

        self._setup()

    def _setup(self) -> None:
        self._canvas = Canvas(self._master, width=self._width, height=self._height, bg='white')
        self._canvas.place(relx=0.001, rely=0.07)

        self._canvas.bind("<Button-1>", self._on_canvas_mouse_button_1_press)
        self._canvas.bind("<ButtonRelease-1>", self._on_canvas_mouse_button_1_release)
        self._canvas.bind("<B1-Motion>", self._on_canvas_mouse_move)

        self.popup_menu = Menu(self._canvas, tearoff=0)
        self.popup_menu.add_command(label="Clear All", command=self._clear_all_canvas_elements)

        self._canvas.bind("<Button-3>", self.on_canvas_button_3_click)

        self.render()

    def _clear_all_canvas_elements(self):
        self._elements = []
        self._selected_element = None

        self.render()

    def _clear(self, active_element: Optional[BaseElement] = None) -> None:
        self._canvas.delete("all")

        for element in self._elements:
            if active_element and active_element.id == element.id:
                continue
            element.is_active = False

    def render(self, active_element: Optional[BaseElement] = None) -> None:
        self._clear(active_element)

        self._render_grid()

        for element in self._elements:
            element.render(self._canvas)

        if self._movable_element:
            self._movable_element.render(self._canvas)

    def add_element(self, element: BaseElement) -> None:
        element.y = self._get_last_bottom_element_pos_y_with_height() + 10
        element.x = 0

        if not element.is_multiple:
            find_result = next((x for x in self._elements if x.element_type == element.element_type), None)
            if find_result:
                messagebox.showerror(title="Ошибка", message="Элемент уже есть на форме")
                return

        self._elements.append(element)

        self.render(element)

    def _on_canvas_mouse_button_1_release(self, event) -> None:
        logger.debug('ChartCanvas - mouse release')

        x = event.x
        y = event.y

        if self._movable_element:
            element = self._selected_element
            if not self._detect_move_collision(self._movable_element):
                self._selected_element.x = x
                self._selected_element.y = y
            self._movable_element = None
        else:
            element = self._is_element_click(x, y)
            if element:
                element.is_active = True

        self.render(element)

    def _on_canvas_mouse_button_1_press(self, event) -> None:
        logger.debug('ChartCanvas - mouse press')

        x = event.x
        y = event.y

        element = self._is_element_click(x, y)
        if element:
            self._selected_element = element

    def _on_canvas_mouse_move(self, event) -> None:
        logger.debug('ChartCanvas - mouse move')

        if self._selected_element:
            if not self._movable_element:
                self._movable_element = deepcopy(self._selected_element)
                self._movable_element.is_movable = True

            if not self._detect_move_collision(self._movable_element):
                self._movable_element.x = event.x
                self._movable_element.y = event.y

            self.render(self._selected_element)

    def on_canvas_button_3_click(self, event) -> None:
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

    def _detect_move_collision(self, moved_element: BaseElement) -> bool:
        for element in self._elements:
            if moved_element.id == element.id:
                continue
            if detect_element_collision(moved_element, element):
                return True
        return False

    def _is_element_click(self, x: int, y: int) -> Optional[BaseElement]:
        for element in self._elements:
            if element.is_point_in_element(x, y):
                return element
        return None

    def _render_grid(self) -> None:
        if not self._is_need_render_grid:
            return

        grid_col_step = 30
        for value in range(0, self._width, grid_col_step):
            self._canvas.create_line(value, 0, value, self._height, dash=(10, 10))

        grid_row_step = 30
        for value in range(0, self._height, grid_row_step):
            self._canvas.create_line(0, value, self._width, value, dash=(10, 10))

    def _get_last_bottom_element_pos_y_with_height(self) -> int:
        if not self._elements:
            return 0

        value = 0
        for element in self._elements:
            if element.y + element.height > value:
                value = element.y + element.height

        return value
