import logging
from tkinter import Frame, BOTH, Tk, TOP, Text, Scrollbar, Button

from src.chart_canvas import ChartCanvas
from src.elements_frame import ElementsFrame
from src.menu import Menu

logger = logging.getLogger(__name__)


class App(Frame):
    def __init__(self, master: Tk, cnf: dict = {}, **kw) -> None:
        logger.info('Start create app')
        super().__init__(master, cnf, **kw)
        self._master = master

        self._APP_WIDTH = 800
        self._APP_HEIGHT = 700
        self._APP_POS_X = 500
        self._APP_POS_Y = 200

        self._setup()

    def _setup(self) -> None:
        self._master.title("Simple")
        self._master.geometry(f"{self._APP_WIDTH}x{self._APP_HEIGHT}+{self._APP_POS_X}+{self._APP_POS_Y}")
        self._master.resizable(False, False)

        self._menu = Menu(self._master)

        self._chart_canvas = ChartCanvas(self._master)

        self._elements_frame = ElementsFrame(self._master, self._chart_canvas)
        self._elements_frame.place(relx=0, rely=0)

        self._text = Text(width=47, height=35)
        self._text.place(relx=0.5, rely=0.07)

        scroll = Scrollbar(command=self._text.yview)
        scroll.place(relx=0.98, rely=0.07)
        self._text.config(yscrollcommand=scroll.set)

        self._generate_btn = Button(text="Generate", width=50)
        self._generate_btn.place(relx=0.25, rely=0.93)
