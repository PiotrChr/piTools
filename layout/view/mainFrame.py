import tkinter
from layout.templating import templating


class MainFrame(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        self.right_frame = None
        self.left_frame = self.get_left_frame(self)

    def pack_all(self):
        self.left_frame.grid(column=0, row=0)
        self.left_frame.pack_propagate(False)

        self.right_frame.grid(column=1, row=0)
        self.right_frame.pack_propagate(False)

        if hasattr(self.right_frame, 'refresh_button'):
            self.right_frame.refresh_button.pack(pady=(20, 0))

        if hasattr(self.right_frame, 'back_button'):
            self.right_frame.back_button.pack(pady=(20, 0))

    def refresh(self):
        pass

    @staticmethod
    def get_left_frame(container):
        left_frame = templating.create_left_frame(container)

        video_frame = tkinter.Label(left_frame)
        video_frame.config(image='')
        video_frame.pack()

        video_frame.current_image = None
        video_frame.imgtk = None

        left_frame.video_frame = video_frame

        return left_frame

    def add_back_button(self):
        back_button = templating.create_back_button(self.right_frame, self.controller.back)
        self.right_frame.back_button = back_button

    def add_refresh_button(self):
        refresh_button = templating.create_refresh_button(self.right_frame, self.refresh)
        self.right_frame.refresh_button = refresh_button
