import tkinter
from layout import view
from layout.templating import templating

class PrinterFrame(view.mainFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.right_frame = self.get_right_frame(self)

    def get_right_frame(self, container):
        # Use helper class here to generate a container
        printer_frame = tkinter.Frame(container)

        frame_label = self.templating.create_medium_label(printer_frame, "3D printer Control")
        frame_label.grid(row=0, columnspan=2, sticky='w')
        printer_frame.frame_label = frame_label

        # # Printer Page
        printer_page_button = templating.create_bar_button(
            printer_frame,
            title="Printer Page",
            action=self.controller.open_printer_page
        )
        printer_page_button.grid(row=1, columnspan=2)
        printer_page_button.camera_start_button = printer_page_button

        # Printer Camera
        camera_frame = self.templating.create_switch_button_frame(
            printer_frame,
            self.start_printer_camera,
            self.stop_printer_camera,
            'Camera'
        )
        printer_frame.camera_frame = camera_frame

        return printer_frame
