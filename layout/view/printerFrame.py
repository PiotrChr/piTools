from layout.view import mainFrame


class PrinterFrame(mainFrame.MainFrame):
    FRAME_LABEL = '3d Printer Control'
    PRINTER_PAGE_BUTTON_LABEL = 'Printer Page'
    CAMERA_BUTTON_LABEL = 'Camera'

    def __init__(self, parent, controller, templating):
        super().__init__(parent, controller, templating)

        self.add_sub_frame_switch()
        self.pack_all()
        self.open_default_sub_frames()

    def create_main_right_frame(self, container):
        right_frame = self.templating.create_right_sub_frame(container)

        # Main Label
        frame_label = self.templating.create_medium_label(right_frame, self.FRAME_LABEL)
        frame_label.pack(pady=20)
        right_frame.set('frame_label', frame_label)

        # Printer Page
        printer_page_button = self.templating.create_bar_button(
            right_frame,
            title=self.PRINTER_PAGE_BUTTON_LABEL,
            action=self.controller.open_printer_page
        )
        printer_page_button.pack()
        right_frame.set('printer_page_button', printer_page_button)

        # Printer Camera
        camera_button = self.templating.create_switch_button_frame(
            right_frame,
            self.controller.start_printer_camera,
            self.controller.stop_printer_camera,
            self.CAMERA_BUTTON_LABEL
        )
        camera_button.pack()
        right_frame.set('camera_button', camera_button)

        return right_frame
