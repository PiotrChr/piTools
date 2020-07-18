import tkinter
from layout import view


class HomeFrame(view.mainFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.right_frame = self.get_right_frame(self)

    def get_right_frame(self, container):
        return 'asd'
