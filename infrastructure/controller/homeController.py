from infrastructure.controller.controller import Controller
from layout.view import printerFrame, securityFrame, statusFrame, antFrame, frontDoorFrame


class HomeController(Controller):
    def __init__(self, layout):
        super().__init__(layout)

    def open_printer(self):
        self.templating.raise_frame(self.layout[printerFrame.PrinterFrame.__name__])

    def open_status(self):
        self.templating.raise_frame(self.layout[statusFrame.StatusFrame.__name__])

    def open_security(self):
        self.templating.raise_frame(self.layout[securityFrame.SecurityFrame.__name__])

    def open_ant(self):
        self.templating.raise_frame(self.layout[antFrame.AntFrame.__name__])

    def open_front_door(self):
        self.templating.raise_frame(self.layout[frontDoorFrame.FrontDoorFrame.__name__])
