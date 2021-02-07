from infrastructure.controller.controller import Controller
from layout.view import printerFrame, securityFrame, statusFrame, antFrame, frontDoorFrame


class HomeController(Controller):
    def __init__(self, templating, layout):
        super().__init__(templating, layout)

    def open_printer(self):
        self.templating.raise_frame(self[printerFrame.PrinterFrame.__name__])

    def open_status(self):
        self.templating.raise_frame(self[statusFrame.StatusFrame.__name__])

    def open_security(self):
        self.templating.raise_frame(self[securityFrame.SecurityFrame.__name__])

    def open_ant(self):
        self.templating.raise_frame(self[antFrame.AntFrame.__name__])
