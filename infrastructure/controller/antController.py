from infrastructure.controller.controller import Controller
from layout.view.antFrame import AntFrame


class AntController(Controller):
    def __init__(self, templating, layout):
        super().__init__(templating, layout)

    def start_ant_camera(self):
        self.start_camera(0, AntFrame.__name__)

    def stop_ant_camera(self):
        self.stop_camera()

    def start_ant_stream(self):
        self.not_yet_implemented()

    def stop_ant_stream(self):
        self.not_yet_implemented()

    def start_ant_lights(self):
        self.not_yet_implemented()

    def stop_ant_lights(self):
        self.not_yet_implemented()

    def start_ant_thermostat(self):
        self.not_yet_implemented()

    def stop_ant_thermostat(self):
        self.not_yet_implemented()
