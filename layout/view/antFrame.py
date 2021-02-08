from layout.view import mainFrame


class AntFrame(mainFrame.MainFrame):
    FRAME_LABEL = 'Ant Farm Control'
    ANT_CAMERA_LABEL = 'Camera'
    ANT_STREAM_LABEL = 'Stream'
    ANT_LIGHTS_LABEL = 'Lights'
    ANT_THERMOSTAT_LABEL = 'Thermostat'

    def __init__(self, parent, controller, templating):
        super().__init__(parent, controller, templating)

        self.right_frame = self.get_right_frame(self)
        self.add_back_button()
        self.pack_all()

    def get_right_frame(self, container):
        right_frame = self.templating.create_right_frame(container)

        # Main Label
        frame_label = self.templating.create_medium_label(right_frame, text=self.FRAME_LABEL)
        frame_label.pack()
        right_frame.frame_label = frame_label

        # Camera
        camera_button = self.templating.create_switch_button_frame(
            right_frame,
            self.controller.start_ant_camera,
            self.controller.stop_ant_camera,
            self.ANT_CAMERA_LABEL
        )
        camera_button.pack()
        right_frame.camera_frame = camera_button

        # Stream
        stream_button = self.templating.create_switch_button_frame(
            right_frame,
            self.controller.start_ant_stream,
            self.controller.stop_ant_stream,
            self.ANT_STREAM_LABEL
        )
        stream_button.pack()
        right_frame.stream_frame = stream_button

        # Lights
        lights_button = self.templating.create_switch_button_frame(
            right_frame,
            self.controller.start_ant_lights,
            self.controller.stop_ant_lights,
            self.ANT_LIGHTS_LABEL
        )
        lights_button.pack()
        right_frame.lights_button = lights_button

        # Thermostat
        thermostat_button = self.templating.create_switch_button_frame(
            right_frame,
            self.controller.start_ant_thermostat,
            self.controller.start_ant_thermostat,
            self.ANT_THERMOSTAT_LABEL
        )
        thermostat_button.pack()
        right_frame.thermostat_button = thermostat_button

        return right_frame
