import tkinter
from layout.tkinter import frame


class MainFrame(frame.Frame):
    def __init__(self, parent, controller, templating):
        super().__init__(parent)
        self.templating = templating
        self.controller = controller(layout=parent)
        self.controller.set_templating(templating)

        self.set('left_frame', self.get_left_frame(self))
        self.set('right_frame', self.get_right_frame(self))

    def pack_all(self):
        left_frame = self.get('left_frame')
        left_frame.grid(column=0, row=0)
        left_frame.pack_propagate(False)

        right_frame = self.get('right_frame')
        right_frame.grid(column=1, row=0)
        right_frame.pack_propagate(False)

        refresh_button = right_frame.get('refresh_button')
        back_button = right_frame.get('back_button')

        if refresh_button:
            refresh_button.pack(pady=(20, 0))

        if back_button:
            back_button.pack(pady=(20, 0))

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

        left_frame.set('video_frame', video_frame)

        return left_frame

    def add_back_button(self):
        self.get('right_frame').set(
            'back_button',
            self.templating.create_back_button(
                self.get('right_frame'),
                self.controller.back
            )
        )

    def get_right_frame(self, container):
        pass
