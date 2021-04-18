import tkinter
from layout.view import mainFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


class FrontDoorFrame(mainFrame.MainFrame):
    FRAME_LABEL = 'Front Door Control'
    MAINTENANCE_LABEL = 'Maintenance'
    STATS_LABEL = 'Statistics'
    CAMERA_LABEL = 'Camera'
    RECORD_LABEL = 'Record'
    LISTEN_LABEL = 'Listen'
    LIGHT_LABEL = 'Light'
    CLEAR_MOTION_LABEL = 'Clear motion table'
    CLEAR_LIGHT_LABEL = 'Clear light table'
    CLEAR_ACC_LABEL = 'Clear acc table'
    CLEAR_ALL = 'Clear all tables'
    CONTROLLER_SUB_FRAME = 'controller'
    STATS_SUB_FRAME = 'stats'
    ACC_PLOT_SUB_FRAME = 'acc_plot'

    def __init__(self, parent, controller, templating):
        super().__init__(parent, controller, templating)

        self.add_sub_frame_switch(self.MAIN_FRAME, self.MAINTENANCE_LABEL, self.CONTROLLER_SUB_FRAME)
        self.add_sub_frame_switch(self.MAIN_FRAME, self.STATS_LABEL, self.STATS_SUB_FRAME)
        self.add_sub_frame_switch(self.CONTROLLER_SUB_FRAME)
        self.add_sub_frame_switch(self.STATS_SUB_FRAME)
        self.add_sub_frame_switch()
        self.pack_all()
        self.open_default_sub_frames()

    def create_left_sub_frames(self):
        container = self.get(self.LEFT_FRAME)

        self.add_left_sub_frame(
            self.MAIN_FRAME,
            self.create_main_left_frame(container),
            True
        )

        self.add_left_sub_frame(
            self.STATS_SUB_FRAME,
            self.create_statistics_left_frame(container),
            False
        )

        self.add_left_sub_frame(
            self.ACC_PLOT_SUB_FRAME,
            self.create_plot_light_left_frame(container),
            False
        )

    def create_statistics_left_frame(self, container):
        left_frame = self.templating.create_left_sub_frame(container)

        frame_label = self.templating.create_medium_label(left_frame, 'Statistics')
        frame_label.pack(expand=True)
        left_frame.set(self.FRAME_LABEL, frame_label)

        return left_frame

    def create_plot_light_left_frame(self, container):
        fig, plts = plt.subplots(2)

        left_frame = self.templating.create_left_sub_frame(container)

        frame_label = self.templating.create_medium_label(left_frame, 'Light Plot')
        frame_label.pack()
        left_frame.set(self.FRAME_LABEL, frame_label)

        plot = FigureCanvasTkAgg(fig, master=left_frame)
        plot.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)
        plts[0].plot([12, 3, 45])
        left_frame.set('plot', plot)

        return left_frame

    def create_right_sub_frames(self):
        container = self.get(self.RIGHT_FRAME)

        self.add_right_sub_frame(
            self.MAIN_FRAME,
            self.create_main_right_frame(container),
            True
        )

        self.add_right_sub_frame(
            self.CONTROLLER_SUB_FRAME,
            self.create_controller_right_frame(container),
            False
        )

        self.add_right_sub_frame(
            self.STATS_SUB_FRAME,
            self.create_statistics_right_frame(container),
            False
        )

    def create_statistics_right_frame(self, container):
        right_frame = self.templating.create_right_sub_frame(container)

        # Main Label
        frame_label = self.templating.create_medium_label(right_frame, text=self.FRAME_LABEL)
        frame_label.pack(pady=20)
        right_frame.set(self.FRAME_LABEL, frame_label)

        # Main view
        main_view_button = self.templating.create_bar_button(
            right_frame,
            'Main view',
            self.controller.main_view
        )
        main_view_button.pack(pady=10)
        right_frame.set('main_view_button', main_view_button)

        # Light graph
        light_graph_button = self.templating.create_bar_button(
            right_frame,
            'Light graph',
            lambda: self.open_sub_frame(self.ACC_PLOT_SUB_FRAME, 'left')
        )
        light_graph_button.pack()
        right_frame.set('light_graph_button', light_graph_button)

        # Motion graph
        motion_graph_button = self.templating.create_bar_button(
            right_frame,
            'Motion graph',
            self.controller.acc_graph
        )
        motion_graph_button.pack()
        right_frame.set('motion_graph_button', motion_graph_button)

        # Acc graph
        acc_graph_button = self.templating.create_bar_button(
            right_frame,
            'Acc graph',
            self.controller.acc_graph
        )
        acc_graph_button.pack()
        right_frame.set('acc_graph_button', acc_graph_button)

        return right_frame

    def create_controller_right_frame(self, container):
        right_frame = self.templating.create_right_sub_frame(container)

        # Main Label
        frame_label = self.templating.create_medium_label(right_frame, text=self.FRAME_LABEL)
        frame_label.pack(pady=20)
        right_frame.set(self.FRAME_LABEL, frame_label)

        # Clear All
        clear_all_button = self.templating.create_bar_button(
            right_frame,
            self.CLEAR_ALL,
            self.controller.clear_all,
            'red'
        )
        clear_all_button.pack()
        right_frame.set('clear_db_button', clear_all_button)

        # Clear ACC
        clear_acc_button = self.templating.create_bar_button(
            right_frame,
            self.CLEAR_ACC_LABEL,
            self.controller.clear_acc,
            'yellow'
        )
        clear_acc_button.pack()
        right_frame.set('clear_acc_button', clear_acc_button)

        # Clear Light
        clear_light_button = self.templating.create_bar_button(
            right_frame,
            self.CLEAR_LIGHT_LABEL,
            self.controller.clear_light,
            'yellow'
        )
        clear_light_button.pack()
        right_frame.set('clear_light_button', clear_light_button)

        # Clear Motion
        clear_motion_button = self.templating.create_bar_button(
            right_frame,
            self.CLEAR_MOTION_LABEL,
            self.controller.clear_motion,
            'yellow'
        )
        clear_motion_button.pack()
        right_frame.set('clear_motion_button', clear_motion_button)

        return right_frame

    def create_main_right_frame(self, container):
        right_frame = self.templating.create_right_sub_frame(container)

        # Main Label
        frame_label = self.templating.create_medium_label(right_frame, text=self.FRAME_LABEL)
        frame_label.pack(pady=20)
        right_frame.set(self.FRAME_LABEL, frame_label)

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
