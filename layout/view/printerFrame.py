from layout.view import mainFrame
from layout.templating import templating


class PrinterFrame(mainFrame.MainFrame):
    FRAME_LABEL = '3d Printer Control'
    PRINTER_PAGE_BUTTON_LABEL = 'Printer Page'
    CAMERA_BUTTON_LABEL = 'Camera'

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

        # Printer Page
        printer_page_button = templating.create_bar_button(
            right_frame,
            title=self.PRINTER_PAGE_BUTTON_LABEL,
            action=self.controller.open_printer_page
        )
        printer_page_button.pack()
        printer_page_button.printer_page_button = printer_page_button

        # Printer Camera
        camera_button = templating.create_switch_button_frame(
            right_frame,
            self.controller.start_printer_camera,
            self.controller.stop_printer_camera,
            self.CAMERA_BUTTON_LABEL
        )
        camera_button.pack()
        right_frame.camera_button = camera_button

        return right_frame
