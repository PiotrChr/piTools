from infrastructure.controller.controller import Controller
from layout.view.printerFrame import PrinterFrame
from library.sysUtils import SysUtils
import settings


class PrinterController(Controller):
    def __init__(self, templating, layout):
        super().__init__(templating, layout)

    def start_printer_camera(self):
        try:
            SysUtils.validate_host(settings.PRINTER_BASE_URL, settings.PRINTER_STREAM_URL)
        except Exception as exception:
            self.templating.errorbox(message=str(exception))
            return

        self.start_camera(settings.PRINTER_STREAM_URL, PrinterFrame.__name__)

    def stop_printer_camera(self):
        self.stop_camera()

    def open_printer_page(self):
        self.not_yet_implemented()
