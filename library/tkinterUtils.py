from tkinter import *
from tkinter import messagebox


class TkinterTemplating:
    def __init__(self, switch_text_on=None, switch_text_off=None, button_text_back=None, button_text_refresh=None,
                 button_width=None, button_height=None, font_size=None,
                 font_family=None, font_size_big=None, font_size_small=None, frame_height=None, frame_width=None,
                 left_right_ratio=None, color=None):
        self.switch_text_on = switch_text_on
        self.switch_text_off = switch_text_off
        self.button_text_back = button_text_back
        self.button_text_refresh = button_text_refresh
        self.button_width = button_width
        self.button_height = button_height
        self.font_size = font_size
        self.font_size_big = font_size_big
        self.font_size_small = font_size_small
        self.font_family = font_family
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.left_right_ratio = left_right_ratio
        self.color = color
        self.font_bold = font_family + ' ' + str(font_size) + ' ' + 'bold'

    def create_medium_label(self, container, text):
        return Label(container, text=text, height=1, anchor='e', font=(self.font_family, self.font_size_big))

    def create_small_label(self, container, text):
        return Label(container, text=text, height=1, font=(self.font_family, self.font_size))

    def create_keyval_label(self, container, key, value, label=None):
        keyval_frame = Frame(container)

        row = 0
        if label:
            keyval_label = Label(keyval_frame, text=label)
            keyval_label.grid(row=row, column=0, columnspan=2)
            row = row + 1

        key_text = Label(keyval_frame, width=20, font=self.font_bold, text=key, anchor="w")
        key_text.grid(row=row, column=0, sticky=W)
        keyval_frame.key_text = key_text

        value_text = Label(keyval_frame, text=value, anchor="w")
        value_text.grid(row=row, column=1, sticky=E)
        keyval_frame.value_text = value_text

        return keyval_frame

    def create_switch_button_frame(self, container, action_on, action_off, label=None, label_on=None,
                                   label_off=None):
        button_frame = Frame(container)

        row = 0
        if label:
            button_label = self.create_small_label(button_frame, text=label)
            button_frame.button_label = button_label
            button_label.grid(column=0, columnspan=2, row=row)
            row = row + 1

        on_button = self.create_button(
            button_frame,
            text=label_on or self.switch_text_on,
            command=action_on,
            width=(self.button_width // 2) - 2,
            height=self.button_height,
            bg=self.color['lightgreen']
        )
        on_button.grid(column=0, row=row)
        button_frame.on_button = on_button

        off_button = self.create_button(
            button_frame,
            text=label_off or self.switch_text_off,
            command=action_off,
            width=(self.button_width // 2) - 2,
            height=self.button_height,
            bg=self.color['lightred']
        )
        off_button.grid(column=1, row=row)
        button_frame.off_button = off_button

        return button_frame

    def create_bar_button(self, container, title=None, action=None, bg=None):
        return self.create_button(
            container,
            text=title,
            command=action,
            width=self.button_width,
            height=self.button_height,
            bg=bg
        )

    @staticmethod
    def create_button(container, text=None, command=None, width=None, height=None, bg=None, fg='black'):
        button = Button(
            container,
            text=text,
            command=command,
            width=width,
            height=height
        )

        if bg:
            button.configure(highlightbackground=bg, fg=fg, highlightthickness=1)
            # if settings.IS_OSX:
            #     button.configure(highlightbackground=bg, fg=fg, highlightthickness=1)
            # else:
            #     button.configure(bg=bg, fg=fg)

        return button

    def create_back_button(self, container, action):
        return self.create_bar_button(container, self.button_text_back, action, bg=self.color['lightgreen'])

    def create_refresh_button(self, container, action):
        return self.create_bar_button(container, self.button_text_refresh, action, bg=self.color['lightgreen'])

    def create_slider(self, container, from_=None, to=None, horizontal=True, command=None):
        slider = Scale(
            container,
            from_=from_,
            to=to,
            length=self.button_width,
            orient=HORIZONTAL if horizontal else VERTICAL,
            command=command
        )

        return slider

    def create_slider_label(self, container, title=None, description=None, command=None, from_=None, to=None):
        slider_frame = Frame(container)

        slider_label = self.create_medium_label(slider_frame, title)
        slider_frame.slider_label = slider_label

        slider_description = self.create_small_label(slider_frame, description)
        slider_frame.slider_description = slider_description

        slider = self.create_slider(slider_frame, from_=from_, to=to, command=command)
        slider_frame.slider = slider

        slider_description.pack()
        slider_label.pack()
        slider.pack()
        return slider_frame

    def create_simple_slider_label(self, container, title=None, description=None, command=None):
        return self.create_slider_label(container, title, description, from_=0, to=100, command=command)

    @staticmethod
    def raise_frame(frame):
        frame.tkraise()

    def create_right_frame(self, container):
        right_frame = Frame(
            container,
            width=self.frame_width * (1 - self.left_right_ratio),
            height=self.frame_height,
            # bg='orange',
            # borderwidth=1,
            # relief="solid",
        )
h
        return right_frame

    def create_left_frame(self, container):
        left_frame = Frame(
            container,
            width=self.frame_width * self.left_right_ratio,
            height=self.frame_height,
            # bg='violet',
        )

        return left_frame

    @staticmethod
    def infobox(title="Info", message=None):
        messagebox.showinfo(title, message)

    @staticmethod
    def errorbox(title="Error", message=None):
        messagebox.showerror(title, message)
