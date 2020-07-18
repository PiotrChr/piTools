import tkinter
from layout import view


class AntFrame(view.mainFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.right_frame = self.get_right_frame(self)

    def get_right_frame(self, container):
        ant_frame = tkinter.Frame(container)

        frame_label = self.templating.create_medium_label(ant_frame, text="Ant Control")
        frame_label.grid(row=0, columnspan=2, sticky='w')
        ant_frame.frame_label = frame_label

        # Camera
        camera_frame = self.templating.create_switch_button_frame(
            ant_frame,
            self.start_ant_camera,
            self.stop_ant_camera,
            'Camera'
        )
        ant_frame.camera_frame = camera_frame

        # Stream
        stream_frame = self.templating.create_switch_button_frame(
            ant_frame,
            self.start_ant_stream,
            self.stop_ant_stream,
            'Stream'
        )
        ant_frame.stream_frame = stream_frame

        # Lights
        lights_frame = self.templating.create_switch_button_frame(
            ant_frame,
            self.start_ant_lights,
            self.stop_ant_lights,
            'Lights'
        )
        ant_frame.lights_frame = lights_frame

        # Thermostat
        thermostat_frame = self.templating.create_switch_button_frame(
            ant_frame,
            self.start_ant_thermostat,
            self.start_ant_thermostat,
            'Thermostat'
        )
        ant_frame.thermostat_frame = thermostat_frame

        return ant_frame
