import tkinter


class MainFrame(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller

        self.right_frame = None
        self.left_frame = None

    @staticmethod
    def get_left_frame(container):
        left_frame = tkinter.Frame(container)

        video_frame = tkinter.Frame(left_frame)
        left_frame.video_frame = video_frame

        return left_frame
