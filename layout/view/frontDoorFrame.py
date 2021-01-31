from layout.view import mainFrame
from layout.templating import templating


class FrontDoorFrame(mainFrame.MainFrame):
    FRAME_LABEL = 'Front Door Control'
    CAMERA_LABEL = 'Camera'
    RECORD_LABEL = 'Record'
    LISTEN_LABEL = 'Listen'

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.right_frame = self.get_right_frame(self)
        self.add_back_button()
        self.pack_all()

    def get_right_frame(self, container):
        right_frame = templating.create_right_frame(container)

        # Main Label
        frame_label = templating.create_medium_label(right_frame, text=self.FRAME_LABEL)
        frame_label.pack()
        right_frame.frame_label = frame_label

        # Camera
        right_frame.camera_button = templating.create_switch_button_frame(
            right_frame,
            self.controller.start_door_camera,
            self.controller.stop_door_camera,
            self.CAMERA_LABEL
        )
        right_frame.camera_button.pack()

        # Record
        right_frame.record_button = templating.create_switch_button_frame(
            right_frame,
            self.controller.start_door_record,
            self.controller.stop_door_record,
            self.RECORD_LABEL
        )
        right_frame.record_button.pack()

        # Listen
        right_frame.listen_button = templating.create_switch_button_frame(
            right_frame,
            self.controller.start_door_listen,
            self.controller.stop_door_listen,
            self.LISTEN_LABEL
        )
        right_frame.listen_button.pack()

        return right_frame
