from layout.view import mainFrame
from layout.templating import templating


class StatusFrame(mainFrame.MainFrame):
    FRAME_LABEL = 'Status'
    QUIT_BUTTON_LABEL = 'Quit'
    RESTART_BUTTON_LABEL = 'Restart'
    HALT_BUTTON_LABEL = 'Halt'

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.right_frame = self.get_right_frame(self)
        self.add_back_button()
        self.pack_all()

    def get_right_frame(self, container):
        right_frame = templating.create_right_frame(container)

        # Main Label
        frame_label = templating.create_medium_label(right_frame, self.FRAME_LABEL)
        frame_label.pack()
        right_frame.frame_label = frame_label

        # Quit
        quit_button = templating.create_bar_button(
            right_frame,
            title=self.QUIT_BUTTON_LABEL,
            action=self.controller.quit
        )
        quit_button.pack()
        right_frame.quit_button = quit_button

        # Restart
        restart_button = templating.create_bar_button(
            right_frame,
            title=self.RESTART_BUTTON_LABEL,
            action=self.controller.restart
        )
        restart_button.pack()
        right_frame.restart_button = restart_button

        # Halt
        halt_button = templating.create_bar_button(
            right_frame,
            title=self.HALT_BUTTON_LABEL,
            action=self.controller.halt
        )
        halt_button.pack()
        right_frame.halt_button = halt_button

        return right_frame
