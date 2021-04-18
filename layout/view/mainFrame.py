import tkinter
from layout.tkinter import frame


class MainFrame(frame.Frame):
    LEFT_FRAME = 'left_frame'
    RIGHT_FRAME = 'right_frame'
    MAIN_FRAME = 'main'
    VIDEO_FRAME = 'video_frame'
    FRAME_LABEL = 'frame_label'
    REFRESH_BUTTON = 'refresh_button'
    BACK_BUTTON = 'Back'

    def __init__(self, parent, controller, templating):
        super().__init__(parent)
        self.templating = templating
        self.controller = controller(layout=parent)
        self.controller.set_templating(templating)

        self.create_right_frame()
        self.create_left_frame()

        self.create_left_sub_frames()
        self.create_right_sub_frames()

    def create_left_sub_frames(self):
        container = self.get(self.LEFT_FRAME)

        self.add_left_sub_frame(
            self.MAIN_FRAME,
            self.create_main_left_frame(container),
            True
        )

    def create_right_sub_frames(self):
        container = self.get(self.RIGHT_FRAME)

        self.add_right_sub_frame(
            self.MAIN_FRAME,
            self.create_main_right_frame(container),
            True
        )

    def create_main_left_frame(self, container):
        left_frame = self.templating.create_left_sub_frame(container)

        video_frame = tkinter.Label(left_frame)
        video_frame.config(image='')
        video_frame.pack()

        video_frame.current_image = None
        video_frame.imgtk = None

        left_frame.set(self.VIDEO_FRAME, video_frame)

        return left_frame

    def create_main_right_frame(self, container):
        right_frame = self.templating.create_right_sub_frame(container)

        # Main Label
        frame_label = self.templating.create_medium_label(right_frame, 'Template')
        frame_label.pack(pady=20)
        right_frame.set(self.FRAME_LABEL, frame_label)

        return right_frame

    def create_right_frame(self):
        right_frame = self.templating.create_right_frame(self)

        self.set(self.RIGHT_FRAME, right_frame)

    def create_left_frame(self):
        left_frame = self.templating.create_left_frame(self)

        self.set(self.LEFT_FRAME, left_frame)

    def open_sub_frame(self, sub_frame_name, side=None):
        if side is not 'right':
            for name, left_sub_frame in self.get_left_sub_frames().items():
                if name is sub_frame_name:
                    self.controller.open_frame(left_sub_frame['frame'])

        if side is not 'left':
            for name, right_sub_frame in self.get_right_sub_frames().items():
                if name is sub_frame_name:
                    self.controller.open_frame(right_sub_frame['frame'])

    def open_default_sub_frames(self):
        for name, left_sub_frame in self.get_left_sub_frames().items():
            if left_sub_frame['default']:
                self.controller.open_frame(left_sub_frame['frame'])

        for name, right_sub_frame in self.get_right_sub_frames().items():
            if right_sub_frame['default']:
                self.controller.open_frame(right_sub_frame['frame'])

    def get_left_sub_frame(self, name):
        return self.get(self.LEFT_FRAME).sub_frames[name]

    def get_right_sub_frame(self, name):
        return self.get(self.RIGHT_FRAME).sub_frames[name]

    def get_left_sub_frames(self):
        return self.get(self.LEFT_FRAME).sub_frames

    def get_right_sub_frames(self):
        return self.get(self.RIGHT_FRAME).sub_frames

    def add_left_sub_frame(self, frame_name, sub_frame, default=False):
        self.get(self.LEFT_FRAME).sub_frames[frame_name] = {
            'frame': sub_frame,
            'default': default
        }

    def add_right_sub_frame(self, frame_name, sub_frame, default=False):
        self.get(self.RIGHT_FRAME).sub_frames[frame_name] = {
            'frame': sub_frame,
            'default': default
        }

    def pack_all(self):
        for name, left_sub_frame in self.get_left_sub_frames().items():
            left_sub_frame['frame'].grid(row=0, column=0)
            left_sub_frame['frame'].pack_propagate(False)

        for name, right_sub_frame in self.get_right_sub_frames().items():
            right_sub_frame['frame'].grid(row=0, column=0)
            right_sub_frame['frame'].pack_propagate(False)

        left_frame = self.get(self.LEFT_FRAME)
        left_frame.grid(column=0, row=0)
        left_frame.pack_propagate(False)

        right_frame = self.get(self.RIGHT_FRAME)
        right_frame.grid(column=1, row=0)
        right_frame.pack_propagate(False)

        for sf_key, sub_frame in self.get_right_sub_frames().items():
            for key, item in sub_frame['frame'].data.items():
                if self.REFRESH_BUTTON in key:
                    item.pack(pady=(20, 0))

                if self.BACK_BUTTON in key:
                    item.pack(pady=(20, 0))

    def bind_events(self):
        pass

    def register_event_handlers(self):
        pass

    def add_sub_frame_switch(self, sub_frame_name=None, text=None, target_frame_name=None):
        if not sub_frame_name:
            sub_frame_name = self.MAIN_FRAME

        if not text:
            text = self.BACK_BUTTON

        if not target_frame_name:
            target_frame_name = self.MAIN_FRAME

        sub_frame = self.get_right_sub_frame(sub_frame_name)['frame']

        sub_frame.set(
            '%s_%s_%s' % (self.BACK_BUTTON, sub_frame, target_frame_name),
            self.templating.create_back_button(
                sub_frame,
                self.controller.back if (
                    sub_frame_name is self.MAIN_FRAME
                    and target_frame_name is self.MAIN_FRAME
                )
                else lambda: self.open_sub_frame(
                    target_frame_name
                ),
                text
            )
        )

    def get_main_right_frame(self, container):
        pass
