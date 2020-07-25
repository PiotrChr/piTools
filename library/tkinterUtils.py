import tkinter


class TkinterTemplating:
    def __init__(self, switch_text_on=None, switch_text_off=None, button_text_back=None, button_width=None, button_height=None, font_size=None,
                 font_family=None, font_size_big=None, font_size_small=None, frame_height=None, frame_width=None,
                 left_right_ratio=None):
        self.switch_text_on = switch_text_on
        self.switch_text_off = switch_text_off
        self.button_text_back = button_text_back
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

        row = 0
        if label:
            button_label = self.create_small_label(button_frame, text=label)
            button_frame.button_label = button_label
            button_label.grid(column=0, columnspan=2, row=row)
            row = row+1

        on_button = tkinter.Button(button_frame, text=label_on or self.switch_text_on, command=action_on,
                                   width=(self.button_width // 2) - 2,
                                   height=self.button_height)
        on_button.grid(column=0, row=row)
        button_frame.on_button = on_button

        off_button = tkinter.Button(button_frame, text=label_off or self.switch_text_off, command=action_off,
                                    width=(self.button_width // 2) - 2,
                                    height=self.button_height)
        off_button.grid(column=1, row=row)
        button_frame.off_button = off_button

        return button_frame

    def create_bar_button(self, container, title=None, action=None):
        button = tkinter.Button(
            container,
            text=title,
            command=action,
            width=self.button_width,
            height=self.button_height
        )

        return button

    def create_back_button(self, container, action):
        button = tkinter.Button(
            container,
            text=self.button_text_back,
            command=action,
            width=self.button_width,
            height=self.button_height
        )

        return button

    @staticmethod
    def raise_frame(frame):
        frame.tkraise()

    def create_right_frame(self, container):
        right_frame = tkinter.Frame(
            container,
            width=self.frame_width * (1-self.left_right_ratio),
            height=self.frame_height,
            bg='orange'
        )

        return right_frame

    def create_left_frame(self, container):
        left_frame = tkinter.Frame(
            container,
            width=self.frame_width * self.left_right_ratio,
            height=self.frame_height,
            bg='violet'
        )

        return left_frame
