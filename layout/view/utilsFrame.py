from layout.tkinter import frame
from tkinter import Grid

class UtilsFrame(frame.Frame):

    def __init__(self, parent, controller, templating):
        super().__init__(
            parent,
            width=templating.frame_width,
            height=templating.utils_frame_height,
            bg='violet',
            # borderwidth=2
        )
        self.controller = controller(layout=parent)
        self.controller.set_templating(templating)
        self.templating = templating
        # self.bind_events()

        for i, section in enumerate(self.get_sections()):
            section[1].grid(row=0, column=i, sticky="snew")
            Grid.columnconfigure(section[1], i, weight=1)
            section[1].pack_propagate(True)
            self.set(section[0], section[1])

    def get_sections(self):
        return [
            ['system_section', self.get_system_section()]
        ]

    def get_system_section(self):
        system_section = self.templating.create_utils_section(self)

        go_home = self.templating.create_utils_button(
            system_section,
            text='Home',
            command=self.controller.go_home
        )
        go_home.pack(side='left')
        system_section.set('go_home', go_home)

        screen_keyboard_button = self.templating.create_utils_button(
            system_section,
            text='Screen Keyboard',
            command=self.controller.start_screen_keyboard
        )
        screen_keyboard_button.pack(side='left')
        system_section.set('screen_keyboard_button', screen_keyboard_button)

        return system_section


