from layout.view import mainFrame
from layout.templating import templating
from library.sysUtils import SysUtils
import tkinter


class StatusFrame(mainFrame.MainFrame):
    FRAME_LABEL = 'Status'
    QUIT_BUTTON_LABEL = 'Quit'
    RESTART_BUTTON_LABEL = 'Restart'
    HALT_BUTTON_LABEL = 'Halt'

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.right_frame = self.get_right_frame(self)
        self.add_refresh_button()
        self.add_back_button()
        self.pack_all()

    def get_left_frame(self, container):
        left_frame = templating.create_left_frame(container)

        status_section = tkinter.Frame(left_frame)
        status_section.pack(expand=True)

        # Host Uptime label
        host_uptime_label = templating.create_keyval_label(status_section, 'Host uptime: ', SysUtils.uptime())
        host_uptime_label.pack(fill="x")
        status_section.host_uptime_label = host_uptime_label

        # Host Device label
        host_dev_label = templating.create_keyval_label(status_section, 'Host Device: ', SysUtils.host_device())
        host_dev_label.pack(fill="x")
        status_section.host_dev_label = host_dev_label

        # Host IP label
        host_ip_label = templating.create_keyval_label(status_section, 'Host IP: ', SysUtils.host_ip())
        host_ip_label.pack(fill="x")
        status_section.host_ip_label = host_ip_label

        # Host Name label
        host_name_label = templating.create_keyval_label(status_section, 'Host Name: ', SysUtils.host_name())
        host_name_label.pack(fill="x")
        status_section.host_name_label = host_name_label

        left_frame.status_section = status_section

        return left_frame

    def get_right_frame(self, container):
        right_frame = templating.create_right_frame(container)

        # Main Label
        frame_label = templating.create_medium_label(right_frame, self.FRAME_LABEL)
        frame_label.pack()
        right_frame.frame_label = frame_label

        # Quit
        quit_button = templating.create_bar_button(
            right_frame,
            title=self.QUIT_BUTTON_LABEL,
            action=self.controller.quit,
            bg='yellow'
        )
        quit_button.pack()
        right_frame.quit_button = quit_button

        # Restart
        restart_button = templating.create_bar_button(
            right_frame,
            title=self.RESTART_BUTTON_LABEL,
            action=self.controller.restart,
            bg='orange'
        )
        restart_button.pack()
        right_frame.restart_button = restart_button

        # Halt
        halt_button = templating.create_bar_button(
            right_frame,
            title=self.HALT_BUTTON_LABEL,
            action=self.controller.halt,
            bg='red'
        )
        halt_button.pack()
        right_frame.halt_button = halt_button

        return right_frame

    def refresh(self):
        self.left_frame.status_section.host_uptime_label.value_text.config(text=SysUtils.uptime())
