import tkinter


class TkinterTemplating:
    def __init__(self, switch_text_on=None, switch_text_off=None, button_width=None, button_height=None, font_size=None,
                 font_family=None, font_size_big=None, font_size_small=None, frame_height=None, frame_width=None,
                 left_right_ratio=None):
        self.switch_text_on = switch_text_on
        self.switch_text_off = switch_text_off
        self.button_width = button_width
        self.button_height = button_height
        self.font_size = font_size
        self.font_size_big = font_size_big
        self.font_size_small = font_size_small
        self.font_family = font_family
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.left_right_ratio = left_right_ratio

    def create_medium_label(self, container, text):
        return tkinter.Label(container, text=text, height=1, anchor='e', font=(self.font_family, self.font_size_big))

    def create_small_label(self, container, text):
        return tkinter.Label(container, text=text, height=1, font=(self.font_family, self.font_size))

    def create_switch_button_frame(self, container, action_off, action_on, label=None, label_on=None,
                                   label_off=None):
        button_frame = tkinter.Frame(container)

        if label:
            button_label = self.create_small_label(button_frame, text=label)
            button_label.grid(row=1, columnspan=2, sticky='w')

        on_button = tkinter.Button(button_frame, text=label_on and self.switch_text_on, command=action_on,
                                   width=self.button_width / 2,
                                   height=self.button_height)
        on_button.grid(row=2, column=0, sticky='w')
        button_frame.on_button = on_button

        off_button = tkinter.Button(container, text=label_off and self.switch_text_off, command=action_off,
                                    width=self.button_width / 2,
                                    height=self.button_height)
        off_button.grid(row=2, column=1)
        button_frame.camera_stop_button = off_button

        return button_frame

        # TODO: Here
    def create_main_frame(self, container, right_container_items):
        main_frame = tkinter.Frame(container)

        left_frame = tkinter.Frame(main_frame)

        right_frame = tkinter.Frame(main_frame)

        for k, item in enumerate(right_container_items):
            right_frame[k] = item

    @staticmethod
    def raise_frame(frame):
        frame.tkraise()
