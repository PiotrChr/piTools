import tkinter
from layout.tkinter import frame


class MainFrame(frame.Frame):
    def __init__(self, parent, controller, templating):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller(layout=parent)
        self.templating = templating

        self.right_frame = None
        self.controller.set_templating(templating)
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

    def bind_events(self):
        pass

    def register_event_handlers(self):
        pass

    def get_left_frame(self, container):
        left_frame = self.templating.create_left_frame(container)

        video_frame = tkinter.Label(left_frame)
        video_frame.config(image='')
        video_frame.pack()

        video_frame.current_image = None
        video_frame.imgtk = None

        left_frame.video_frame = video_frame

        return left_frame

    def add_back_button(self):
        self.right_frame.back_button = self.templating.create_back_button(self.right_frame, self.controller.back)
