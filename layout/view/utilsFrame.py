from layout.tkinter import frame


class UtilsFrame(frame.Frame):

    def __init__(self, parent, controller, templating):
        super().__init__(parent)
        self.controller = controller
        self.templating = templating
        self.width = templating.frame_width
        self.height = templating.utils_frame_height
        # self.bind_events()

        sections = self.get_sections()
        for i, section in sections:
            name = frame.Frame.create_name(section[0].__name__)
            self[name] = section[0](self, section[1], self.templating)
            self[name].grid(row=0, column=i)

    def get_sections(self):
        return [
            self.get_system_section(), self.controller
        ]

    def get_system_section(self):
        system_section = self.templating.create_utils_section(self)

        return system_section


