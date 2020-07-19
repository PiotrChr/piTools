import tkinter
from layout import view
from layout.templating import templating


class StatusFrame(view.mainFrame):
    FRAME_LABEL = 'Status'
    QUIT_BUTTON_LABEL = 'Quit'
    RESTART_BUTTON_LABEL = 'Restart'
    HALT_BUTTON_LABEL = 'Halt'

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.right_frame = self.get_right_frame(self)
        self.left_frame = self.get_left_frame(self)

    def get_right_frame(self, container):
        right_frame = tkinter.Frame(container)

        # Main Label
        frame_label = self.templating.create_medium_label(right_frame, self.FRAME_LABEL)
        frame_label.grid(row=0, columnspan=2, sticky='w')
        right_frame.frame_label = frame_label

        # Quit
        quit_button = templating.create_bar_button(
            right_frame,
            title=self.QUIT_BUTTON_LABEL,
            action=self.controller.quit
        )
        quit_button.grid(row=0, column=1)
        right_frame.quit_button = quit_button

        # Restart
        restart_button = templating.create_bar_button(
            right_frame,
            title=self.RESTART_BUTTON_LABEL,
            action=self.controller.restart
        )
        restart_button.grid(row=1, column=0)
        right_frame.restart_button = restart_button

        # Halt
        halt_button = templating.create_bar_button(
            right_frame,
            title=self.HALT_BUTTON_LABEL,
            action=self.controller.halt
        )
        halt_button.grid(row=1, column=1)
        right_frame.halt_button = halt_button

        return right_frame

    def get_left_frame(self, container):
        return 'asd'
