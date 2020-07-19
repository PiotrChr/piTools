import tkinter
from layout import view
from layout.templating import templating


class PrinterFrame(view.mainFrame):
    FRAME_LABEL = '3d Printer Control'
    PRINTER_PAGE_BUTTON_LABEL = 'Printer Page'
    CAMERA_BUTTON_LABEL = 'Camera'

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

        # # Printer Page
        printer_page_button = templating.create_bar_button(
            right_frame,
            title=self.PRINTER_PAGE_BUTTON_LABEL,
            action=self.controller.open_printer_page
        )
        printer_page_button.grid(row=1, columnspan=2)
        printer_page_button.camera_start_button = printer_page_button

        # Printer Camera
        camera_frame = self.templating.create_switch_button_frame(
            right_frame,
            self.start_printer_camera,
            self.stop_printer_camera,
            self.CAMERA_BUTTON_LABEL
        )
        right_frame.camera_frame = camera_frame

        return right_frame

    def get_left_frame(self, container):
        return 'asd'
