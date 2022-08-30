import logging
from tkinter import *

from src.app import App


def main():
    logging.basicConfig(level=logging.DEBUG)

    root = Tk()
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
