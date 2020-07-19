import tkinter
from layout import view
from layout.templating import templating


class HomeFrame(view.mainFrame):
    FRAME_LABEL = 'Home'
    STATUS_BUTTON_LABEL = 'Status'
    ANT_BUTTON_LABEL = 'Ant Farm'
    PRINTER_BUTTON_LABEL = '3d Printer'

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

        status_button = templating.create_bar_button(
            right_frame,
            self.STATUS_BUTTON_LABEL,
            self.controller.open_status
        )
        right_frame.status_button = status_button

        ant_button = templating.create_bar_button(
            right_frame,
            self.ANT_BUTTON_LABEL,
            self.controller.open_status
        )
        right_frame.ant_button = ant_button

        printer_button = templating.create_bar_button(
            right_frame,
            self.PRINTER_BUTTON_LABEL,
            self.controller.open_status
        )
        right_frame.printer_button = printer_button

        return right_frame

    def get_left_frame(self, contaiener):
        return 'asd'