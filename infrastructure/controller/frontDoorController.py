from infrastructure.controller.controller import Controller
from layout.view.frontDoorFrame import FrontDoorFrame
import settings


class FrontDoorController(Controller):
    def __init__(self, layout):
        super().__init__(layout)

    def start_door_camera(self):
        self.http_client.get(settings.FRONT_DOOR_BASE_URL + settings.FRONT_DOOR_STREAM_START_PATH)
        self.start_camera(
            settings.FRONT_DOOR_BASE_URL + settings.FRONT_DOOR_STREAM_PATH,
            FrontDoorFrame.__name__
        )

    def stop_door_camera(self):
        self.http_client.get(settings.FRONT_DOOR_BASE_URL + settings.FRONT_DOOR_STREAM_STOP_PATH)
        self.stop_camera()

    def stop_door_record(self):
        self.not_yet_implemented()

    def start_door_record(self):
        self.not_yet_implemented()

    def start_door_listen(self):
        self.not_yet_implemented()

    def stop_door_listen(self):
        self.not_yet_implemented()

    def light_on(self):
        self.http_client.get(settings.FRONT_DOOR_BASE_URL + settings.FRONT_DOOR_LIGHT_ON)

    def light_off(self):
        self.http_client.get(settings.FRONT_DOOR_BASE_URL + settings.FRONT_DOOR_LIGHT_OFF)
