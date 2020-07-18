import tkinter
from layout import view
from layout.templating import templating


class StatusFrame(view.mainFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.right_frame = self.get_right_frame(self)

    def get_right_frame(self, container):
        status_section = tkinter.Frame(container)

        quit_button = templating.create_bar_button(status_section, title="Quit", action=self.controller.quit)
        quit_button.grid(row=0, column=1)
        status_section.quit_button = quit_button

        restart_button = templating.create_bar_button(status_section, title="Restart", action=self.controller.restart)
        restart_button.grid(row=1, column=0)
        status_section.restart_button = restart_button

        halt_button = templating.create_bar_button(status_section, title="Halt", action=self.controller.halt)
        halt_button.grid(row=1, column=1)
        status_section.halt_button = halt_button

        return status_section
