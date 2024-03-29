from layout.view import mainFrame


class SecurityFrame(mainFrame.MainFrame):
    FRAME_LABEL = 'Security Control'

    def __init__(self, parent, controller, templating):
        super().__init__(parent, controller, templating)

        self.add_back_button()
        self.pack_all()

    def get_right_frame(self, container):
        right_frame = self.templating.create_right_frame(container)

        # Main Label
        frame_label = self.templating.create_medium_label(right_frame, text=self.FRAME_LABEL)
        frame_label.pack()
        right_frame.set('frame_label', frame_label)

        return right_frame
