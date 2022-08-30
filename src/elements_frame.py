from tkinter import Frame, Tk, Button, LEFT

from src.chart_canvas import ChartCanvas
from src.elements.constants import ElementType
from src.elements.rectang_text_element import RectangleTextElement


class ElementsFrame(Frame):
    def __init__(self, master: Tk, chart_canvas: ChartCanvas, cnf: dict = {}, **kw) -> None:
        super().__init__(master, cnf, **kw)
        self._master = master
        self._chart_canvas = chart_canvas

        self._setup()

    def _setup(self) -> None:
        self._start_btn = Button(text="START", width=3, height=1, command=self._on_start_btn_click)
        self._start_btn.grid(row=0, column=0)

        self._end_btn = Button(text="END", width=3, height=1, command=self._on_end_btn_click)
        self._end_btn.grid(row=0, column=1)

        self._print_btn = Button(text="PRINT", width=3, height=1, command=self._on_print_btn_click)
        self._print_btn.grid(row=0, column=3)

        self._input_btn = Button(text="INPUT", width=3, height=1, command=self._on_print_btn_click)
        self._input_btn.grid(row=0, column=4)

        self._if_btn = Button(text="FOR", width=3, height=1, command=self._on_if_btn_click)
        self._if_btn.grid(row=0, column=5)

        self._for_btn = Button(text="FOR", width=3, height=1, command=self._on_for_btn_click)
        self._for_btn.grid(row=0, column=6)

        self._while_btn = Button(text="WHILE", width=3, height=1, command=self._on_while_btn_click)
        self._while_btn.grid(row=0, column=7)

        self._codeblock_btn = Button(text="CODE", width=3, height=1, command=self._on_codeblock_btn_click)
        self._codeblock_btn.grid(row=0, column=8)

    def _on_start_btn_click(self) -> None:
        self._chart_canvas.add_element(RectangleTextElement("BEGIN", ElementType.START))

    def _on_end_btn_click(self) -> None:
        self._chart_canvas.add_element(RectangleTextElement("END", ElementType.END))

    def _on_print_btn_click(self) -> None:
        self._chart_canvas.add_element(RectangleTextElement("PRINT", ElementType.PRINT, is_multiple=True))

    def _on_input_btn_click(self) -> None:
        self._chart_canvas.add_element(RectangleTextElement("INPUT", ElementType.INPUT, is_multiple=True))

    def _on_if_btn_click(self) -> None:
        pass

    def _on_for_btn_click(self) -> None:
        pass

    def _on_while_btn_click(self) -> None:
        pass

    def _on_codeblock_btn_click(self) -> None:
        pass
