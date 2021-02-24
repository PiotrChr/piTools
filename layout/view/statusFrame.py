from layout.view import mainFrame
from layout.tkinter import frame
from library.sysUtils import SysUtils
import settings


class StatusFrame(mainFrame.MainFrame):
    FRAME_LABEL = 'Status'
    QUIT_BUTTON_LABEL = 'Quit'
    RESTART_BUTTON_LABEL = 'Restart'
    HALT_BUTTON_LABEL = 'Halt'

    def __init__(self, parent, controller, templating):
        super().__init__(parent, controller, templating)

        self.add_refresh_button()
        self.add_back_button()
        self.bind_events()
        self.pack_all()

    def get_left_frame(self, container):
        left_frame = self.templating.create_left_frame(container)

        status_section = frame.Frame(left_frame)
        status_section.pack(expand=True)

        # Host Uptime label
        host_uptime_label = self.templating.create_keyval_label(status_section, 'Host uptime: ', SysUtils.uptime())
        host_uptime_label.pack(fill="x")
        status_section.set('host_uptime_label', host_uptime_label)

        # Host Device label
        host_dev_label = self.templating.create_keyval_label(status_section, 'Host Device: ', SysUtils.host_device())
        host_dev_label.pack(fill="x")
        status_section.set('host_dev_label', host_dev_label)

        # Host IP label
        host_ip_label = self.templating.create_keyval_label(status_section, 'Host IP: ', SysUtils.host_ip())
        host_ip_label.pack(fill="x")
        status_section.set('host_ip_label', host_ip_label)

        # Host Name label
        host_name_label = self.templating.create_keyval_label(status_section, 'Host Name: ', SysUtils.host_name())
        host_name_label.pack(fill="x")
        status_section.set('host_name_label', host_name_label)

        printer_host_up = True
        front_door_host_up = True

        # Printer Host Name label
        printer_host_name_label = self.templating.create_keyval_label(
            status_section,
            'Printer Host Status: ',
            settings.PRINTER_BASE_URL + (' is Up' if printer_host_up else ' is Down')
        )
        printer_host_name_label.pack(fill="x")
        status_section.set('printer_host_name_label', printer_host_name_label)

        # Front Door Host Name label
        front_door_host_name_label = self.templating.create_keyval_label(
            status_section,
            'Front Door Host Status: ',
            settings.FRONT_DOOR_BASE_URL + (' is Up' if front_door_host_up else ' is Down')
        )
        front_door_host_name_label.pack(fill="x")
        status_section.set('front_door_host_name_label', front_door_host_name_label)

        left_frame.set('status_section', status_section)

        return left_frame

    def get_right_frame(self, container):
        right_frame = self.templating.create_right_frame(container)

        # Main Label
        frame_label = self.templating.create_medium_label(right_frame, self.FRAME_LABEL)
        frame_label.pack()
        right_frame.set('frame_label', frame_label)

        # Quit
        quit_button = self.templating.create_bar_button(
            right_frame,
            title=self.QUIT_BUTTON_LABEL,
            action=self.controller.quit,
            bg='yellow'
        )
        quit_button.pack()
        right_frame.set('quit_button', quit_button)

        # Restart
        restart_button = self.templating.create_bar_button(
            right_frame,
            title=self.RESTART_BUTTON_LABEL,
            action=self.controller.restart,
            bg='orange'
        )
        restart_button.pack()
        right_frame.set('restart_button', restart_button)

        # Halt
        halt_button = self.templating.create_bar_button(
            right_frame,
            title=self.HALT_BUTTON_LABEL,
            action=self.controller.halt,
            bg='red'
        )
        halt_button.pack()
        right_frame.set('halt_button', halt_button)

        return right_frame

    def bind_events(self):
        self.bind('<Enter>', self.refresh)

    def refresh(self, event=None):
        printer_host_up = True
        front_door_host_up = True

        self\
            .get('left_frame')\
            .get('status_section')\
            .get('host_uptime_label')\
            .value_text.config(
                text=SysUtils.uptime()
            )

        try:
            SysUtils.validate_host(settings.PRINTER_BASE_URL, is_rasp=settings.IS_RASP)
        except:
            printer_host_up = False

        try:
            SysUtils.validate_host(settings.FRONT_DOOR_BASE_URL, is_rasp=settings.IS_RASP)
        except:
            front_door_host_up = False

        self\
            .get('left_frame')\
            .get('status_section')\
            .get('printer_host_name_label')\
            .value_text.config(
                text=settings.PRINTER_BASE_URL + (' is Up' if printer_host_up else ' is Down')
            )

        self\
            .get('left_frame')\
            .get('status_section')\
            .get('front_door_host_name_label').\
            value_text.config(
                text=settings.FRONT_DOOR_BASE_URL + (' is Up' if front_door_host_up else ' is Down')
            )

    def add_refresh_button(self):
        right_frame = self.get('right_frame')

        refresh_button = self.templating.create_refresh_button(
            right_frame,
            self.refresh
        )
        right_frame.set('refresh_button', refresh_button)
