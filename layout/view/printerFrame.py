import tkinter
from layout import view


class PrinterFrame(view.mainFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
