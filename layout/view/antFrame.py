import tkinter
from layout import view


class AntFrame(view.mainFrame):
    FRAME_LABEL = 'Ant Farm Control'
    ANT_CAMERA_LABEL = 'Camera'
    ANT_STREAM_LABEL = 'Stream'
    ANT_LIGHTS_LABEL = 'Label'
    ANT_THERMOSTAT_LABEL = 'Thermostat'

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.controller = controller
        self.right_frame = self.get_right_frame(self)
        self.left_frame = self.get_left_frame(self)

    def get_right_frame(self, container):
        right_frame = tkinter.Frame(container)

        # Main Label
        frame_label = self.templating.create_medium_label(right_frame, text=self.FRAME_LABEL)
        frame_label.grid(row=0, columnspan=2, sticky='w')
        right_frame.frame_label = frame_label

        # Camera
        camera_frame = self.templating.create_switch_button_frame(
            right_frame,
            self.controller.start_ant_camera,
            self.controller.stop_ant_camera,
            self.ANT_CAMERA_LABEL
        )
        right_frame.camera_frame = camera_frame

        # Stream
        stream_frame = self.templating.create_switch_button_frame(
            right_frame,
            self.controller.start_ant_stream,
            self.controller.stop_ant_stream,
            self.ANT_STREAM_LABEL
        )
        right_frame.stream_frame = stream_frame

        # Lights
        lights_frame = self.templating.create_switch_button_frame(
            right_frame,
            self.controller.start_ant_lights,
            self.controller.stop_ant_lights,
            self.ANT_LIGHTS_LABEL
        )
        right_frame.lights_frame = lights_frame

        # Thermostat
        thermostat_frame = self.templating.create_switch_button_frame(
            right_frame,
            self.controller.start_ant_thermostat,
            self.controller.start_ant_thermostat,
            self.ANT_THERMOSTAT_LABEL
        )
        right_frame.thermostat_frame = thermostat_frame

        return right_frame

