from layout.view import mainFrame
from layout.menu.menu import menu


class HomeFrame(mainFrame.MainFrame):
    FRAME_LABEL = 'Home'
    STATUS_BUTTON_LABEL = 'Status'
    ANT_BUTTON_LABEL = 'Ant Farm'
    PRINTER_BUTTON_LABEL = '3d Printer'

    def __init__(self, parent, controller, templating):
        super().__init__(parent, controller, templating)

        self.pack_all()
        self.open_default_sub_frames()

    def create_main_left_frame(self, container):
        left_frame = self.templating.create_left_sub_frame(container)

        frame_label = self.templating.create_medium_label(left_frame, 'Welcome')
        frame_label.pack(expand=True)
        left_frame.set(self.FRAME_LABEL, frame_label)

        return left_frame

    def create_main_right_frame(self, container):
        right_frame = self.templating.create_right_sub_frame(container)

        # Main Label
        frame_label = self.templating.create_medium_label(right_frame, self.FRAME_LABEL)
        frame_label.pack(pady=20)
        right_frame.set(self.FRAME_LABEL, frame_label)

        # Menu
        for menuItem in menu:
            name = menuItem.id + "_button"
            item = self.templating.create_bar_button(
                right_frame,
                menuItem.title,
                getattr(self.controller, menuItem.action)
            )
            item.pack()
            right_frame.set(name, item)

        return right_frame
