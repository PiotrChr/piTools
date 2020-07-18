import tkinter
from layout import view


class AntFrame(view.mainFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
