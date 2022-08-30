from tkinter import Menu as TkinterMenu, Tk


class Menu:
    def __init__(self, master: Tk) -> None:
        self._master = master
        self._setup()

    def _setup(self) -> None:
        menubar = TkinterMenu(self._master)
        self._master.config(menu=menubar)

        # file menu
        file_menu = TkinterMenu(menubar, tearoff=False)
        file_menu.add_command(label="Выход", underline=0, command=self.on_exit)

        menubar.add_cascade(label="Файл", menu=file_menu)

    def on_exit(self):
        self._master.quit()
