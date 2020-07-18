import tkinter


class MainFrame(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller

        self.right_frame = None
        self.left_frame = self.get_left_frame(self)

    def get_left_frame(self, container):
        left_frame = tkinter.Frame(container)

        return left_frame
