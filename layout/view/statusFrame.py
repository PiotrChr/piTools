from layout.view import mainFrame
from library.sysUtils import SysUtils
import settings
import tkinter


class StatusFrame(mainFrame.MainFrame):
    FRAME_LABEL = 'Status'
    QUIT_BUTTON_LABEL = 'Quit'
    RESTART_BUTTON_LABEL = 'Restart'
    HALT_BUTTON_LABEL = 'Halt'

    def __init__(self, parent, controller, templating):
        super().__init__(parent, controller, templating)

        self.right_frame = self.get_right_frame(self)
        self.add_refresh_button()
        self.add_back_button()
        self.pack_all()

    def get_left_frame(self, container):
        left_frame = self.templating.create_left_frame(container)

        status_section = tkinter.Frame(left_frame)
        status_section.pack(expand=True)

        # Host Uptime label
        status_section.host_uptime_label = self.templating.create_keyval_label(status_section, 'Host uptime: ', SysUtils.uptime())
        status_section.host_uptime_label.pack(fill="x")

        # Host Device label
        status_section.host_dev_label = self.templating.create_keyval_label(status_section, 'Host Device: ', SysUtils.host_device())
        status_section.host_dev_label.pack(fill="x")

        # Host IP label
        status_section.host_ip_label = self.templating.create_keyval_label(status_section, 'Host IP: ', SysUtils.host_ip())
        status_section.host_ip_label.pack(fill="x")

        # Host Name label
        status_section.host_name_label = self.templating.create_keyval_label(status_section, 'Host Name: ', SysUtils.host_name())
        status_section.host_name_label.pack(fill="x")

        printer_host_up = True
        try:
            SysUtils.validate_host(settings.PRINTER_BASE_URL, is_rasp=settings.IS_RASP)
        except:
            printer_host_up = False

        # Printer Host Name label
        status_section.printer_host_name_label = self.templating.create_keyval_label(
            status_section,
            'Printer Host Status: ',
            settings.PRINTER_BASE_URL + (' is Up' if printer_host_up else ' is Down')
        )
        status_section.printer_host_name_label.pack(fill="x")

        # Front Door Host Name label
        status_section.front_door_host_name_label = self.templating.create_keyval_label(
            status_section,
            'Front Door Host Status: ',
            settings.FRONT_DOOR_BASE_URL + (' is Up' if printer_host_up else ' is Down')
        )
        status_section.front_door_host_name_label.pack(fill="x")

        left_frame.status_section = status_section

        return left_frame

    def get_right_frame(self, container):
        right_frame = self.templating.create_right_frame(container)

        # Main Label
        right_frame.frame_label = self.templating.create_medium_label(right_frame, self.FRAME_LABEL)
        right_frame.frame_label.pack()

        # Quit
        right_frame.quit_button = self.templating.create_bar_button(
            right_frame,
            title=self.QUIT_BUTTON_LABEL,
            action=self.controller.quit,
            bg='yellow'
        )
        right_frame.quit_button.pack()

        # Restart
        right_frame.restart_button = self.templating.create_bar_button(
            right_frame,
            title=self.RESTART_BUTTON_LABEL,
            action=self.controller.restart,
            bg='orange'
        )
        right_frame.restart_button.pack()

        # Halt
        right_frame.halt_button = self.templating.create_bar_button(
            right_frame,
            title=self.HALT_BUTTON_LABEL,
            action=self.controller.halt,
            bg='red'
        )
        right_frame.halt_button.pack()

        return right_frame

    def refresh(self):
        self.left_frame.status_section.host_uptime_label.value_text.config(text=SysUtils.uptime())
