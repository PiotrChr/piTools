from layout.view import mainFrame
from layout.templating import templating


class HomeFrame(mainFrame.MainFrame):
    FRAME_LABEL = 'Home'
    STATUS_BUTTON_LABEL = 'Status'
    ANT_BUTTON_LABEL = 'Ant Farm'
    PRINTER_BUTTON_LABEL = '3d Printer'

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.right_frame = self.get_right_frame(self)
        self.pack_all()

    def get_right_frame(self, container):
        right_frame = templating.create_right_frame(container)

        # Main Label
        frame_label = templating.create_medium_label(right_frame, self.FRAME_LABEL)
        frame_label.pack()
        right_frame.frame_label = frame_label

        # Status
        status_button = templating.create_bar_button(
            right_frame,
            self.STATUS_BUTTON_LABEL,
            self.controller.open_status
        )
        status_button.pack()
        right_frame.status_button = status_button

        # Ants
        ant_button = templating.create_bar_button(
            right_frame,
            self.ANT_BUTTON_LABEL,
            self.controller.open_ant
        )
        ant_button.pack()
        right_frame.ant_button = ant_button

        # Printer
        printer_button = templating.create_bar_button(
            right_frame,
            self.PRINTER_BUTTON_LABEL,
            self.controller.open_printer
        )
        printer_button.pack()
        right_frame.printer_button = printer_button

        return right_frame
