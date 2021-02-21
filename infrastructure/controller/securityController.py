from infrastructure.controller.controller import Controller
from layout.view.printerFrame import PrinterFrame
from library.sysUtils import SysUtils
import settings


class SecurityController(Controller):
    def __init__(self, layout):
        super().__init__(layout)
