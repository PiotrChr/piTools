from layout.view import mainFrame


class FrontDoorFrame(mainFrame.MainFrame):
    FRAME_LABEL = 'Front Door Control'
    CAMERA_LABEL = 'Camera'
    RECORD_LABEL = 'Record'
    LISTEN_LABEL = 'Listen'
    LIGHT_LABEL = 'Light'

    def __init__(self, parent, controller, templating):
        super().__init__(parent, controller, templating)

        self.set('right_frame', self.get_right_frame(self))
        self.add_back_button()
        self.pack_all()

    def get_right_frame(self, container):
        right_frame = self.templating.create_right_frame(container)

        # Main Label
        frame_label = self.templating.create_medium_label(right_frame, text=self.FRAME_LABEL)
        frame_label.pack(pady=20)
        right_frame.set('frame_label', frame_label)

        # Camera
        camera_button = self.templating.create_switch_button_frame(
            right_frame,
            self.controller.start_door_camera,
            self.controller.stop_door_camera,
            self.CAMERA_LABEL
        )
        camera_button.pack()
        right_frame.set('camera_button', camera_button)

        # Lights
        light_button = self.templating.create_switch_button_frame(
            right_frame,
            self.controller.light_on,
            self.controller.light_off,
            self.LIGHT_LABEL
        )
        light_button.pack()
        right_frame.set('light_button', light_button)

        # Record
        record_button = self.templating.create_switch_button_frame(
            right_frame,
            self.controller.start_door_record,
            self.controller.stop_door_record,
            self.RECORD_LABEL
        )
        record_button.pack()
        right_frame.set('record_button', record_button)

        # Listen
        listen_button = self.templating.create_switch_button_frame(
            right_frame,
            self.controller.start_door_listen,
            self.controller.stop_door_listen,
            self.LISTEN_LABEL
        )
        listen_button.pack()
        right_frame.set('listen_button', listen_button)

        return right_frame
