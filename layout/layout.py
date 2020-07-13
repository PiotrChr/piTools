import tkinter
from PIL import Image, ImageTk
from library import httpUtils, tkinterUtils
from time import sleep
import cv2
import settings


class ControlCenterGUI:
    BAR_BUTTON_HEIGHT = 2
    BAR_BUTTON_WIDTH = 7

    BUTTON_TEXT_ON = 'Start'
    BUTTON_TEXT_OFF = 'Stop'

    def __init__(self, title):
        self.master = tkinter.Tk()
        self.master.title(title)
        self.stop_camera_signal = False

        self.templating = tkinterUtils.TkinterTemplating(
            switch_text_on=settings.LAYOUT_TEXT_ON,
            switch_text_off=settings.LAYOUT_TEXT_OFF,
            button_width=settings.LAYOUT_BUTTON_WIDTH,
            button_height=settings.LAYOUT_BUTTON_HEIGHT,
            font_size=settings.LAYOUT_FONT_SIZE,
            font_family=settings.LAYOUT_FONT_FAMILY,
            font_size_big=settings.LAYOUT_BIG_FONT_SIZE,
            font_size_small=settings.LAYOUT_SMALL_FONT_SIZE
        )

        self.layout = self.get_layout()

    # def getFrames
    #     return [
    #
    #     ]

    def get_layout(self):
        layout = tkinter.Frame(self.master)
        layout.pack(fill='both', expand=True)

        cameraframe_label = tkinter.Label(layout)
        cameraframe_label.pack(side='left', fill='y', expand=False)
        layout.cameraframe_label = cameraframe_label

        right_bar = self.get_right_bar(layout)
        right_bar.pack(side='right', fill='y', padx=5, pady=5)
        layout.right_bar = right_bar

        return layout

    def update_camera_frame(self, image, imagetk):
        self.layout.cameraframe_label.currentImage = image
        self.layout.cameraframe_label.imgtk = imagetk
        self.layout.cameraframe_label.config(image=imagetk)  # show the image
        self.layout.cameraframe_label.config(image=imagetk)  # show the image

    def get_status_frame(self, container):
        status_frame = tkinter.Frame(container)

        ip_label = tkinter.Label(status_frame, text="Ip:")
        ip_label.grid(row=0, column=0)
        status_frame.ipLabel = ip_label

        ip_value = tkinter.Label(status_frame, text=httpUtils.get_host_ip())
        ip_value.grid(row=0, column=1)
        status_frame.ipValue = ip_value

        host_label = tkinter.Label(status_frame, text="Host:")
        host_label.grid(row=1, column=0)
        status_frame.hostLabel = host_label

        host_value = tkinter.Label(status_frame, text=httpUtils.get_host_name())
        host_value.grid(row=1, column=1)
        status_frame.ipValue = host_value

        return status_frame

    def get_status_section(self, container):
        status_section = tkinter.Frame(container)

        status_button = tkinter.Button(status_section, text="Status", command=self.quit,
                                       width=self.BAR_BUTTON_WIDTH,
                                       height=self.BAR_BUTTON_HEIGHT)
        status_button.grid(row=0, column=0)
        status_section.status_button = status_button

        quit_button = tkinter.Button(status_section, text="Quit", command=self.quit,
                                     width=self.BAR_BUTTON_WIDTH,
                                     height=self.BAR_BUTTON_HEIGHT)
        quit_button.grid(row=0, column=1)
        status_section.quitButton = quit_button

        restart_button = tkinter.Button(status_section, text="Restart", command=self.restart,
                                        width=self.BAR_BUTTON_WIDTH,
                                        height=self.BAR_BUTTON_HEIGHT)
        restart_button.grid(row=1, column=0)
        status_section.restart_button = restart_button

        halt_button = tkinter.Button(status_section, text="Halt", command=self.halt,
                                     width=self.BAR_BUTTON_WIDTH,
                                     height=self.BAR_BUTTON_HEIGHT)
        halt_button.grid(row=1, column=1)
        status_section.halt_button = halt_button

        return status_section

    def get_right_bar(self, container):
        right_bar = tkinter.Frame(container)

        status_section = self.get_status_section(right_bar)
        status_section.grid(row=0)
        right_bar.status_section = status_section

        ant_section = self.get_ant_section(right_bar)
        ant_section.grid(row=1)
        right_bar.antSection = ant_section

        printer_section = self.get_printer_section(right_bar)
        printer_section.grid(row=2)
        right_bar.printerSection = printer_section

        return right_bar

    def get_printer_section(self, container):
        printer_frame = tkinter.Frame(container)

        frame_label = self.templating.create_medium_label(printer_frame, "3D printer Control")
        frame_label.grid(row=0, columnspan=2, sticky='w')
        printer_frame.frame_label = frame_label

        # # Printer Page
        # printerPageButton = tkinter.Button(printerFrame, text='Open printer page', command=self.startAntCamera,
        #                                    width=self.BAR_BUTTON_WIDTH * 2,
        #                                    height=self.BAR_BUTTON_HEIGHT)
        # printerPageButton.grid(row=1, columnspan=2)
        # printerFrame.camera_start_button = printerPageButton

        # Printer Camera
        camera_frame = self.templating.create_switch_button_frame(printer_frame, self.start_printer_camera,
                                                                  self.stop_printer_camera, 'Camera')
        printer_frame.camera_frame = camera_frame

        return printer_frame

    def get_ant_section(self, container):
        ant_frame = tkinter.Frame(container)

        frame_label = self.templating.create_medium_label(ant_frame, text="Ant Control")
        frame_label.grid(row=0, columnspan=2, sticky='w')
        ant_frame.frame_label = frame_label

        # Camera
        camera_frame = self.templating.create_switch_button_frame(ant_frame, self.start_ant_camera,
                                                                  self.stop_ant_camera, 'Camera')
        ant_frame.camera_frame = camera_frame

        # Stream
        stream_frame = self.templating.create_switch_button_frame(ant_frame, self.start_ant_stream,
                                                                  self.stop_ant_stream, 'Stream')
        ant_frame.stream_frame = stream_frame

        # Lights
        lights_frame = self.templating.create_switch_button_frame(ant_frame, self.start_ant_lights,
                                                                  self.stop_ant_lights, 'Lights')
        ant_frame.lights_frame = lights_frame

        # Thermostat
        thermostat_frame = self.templating.create_switch_button_frame(ant_frame, self.start_ant_thermostat,
                                                                      self.start_ant_thermostat, 'Thermostat')
        ant_frame.thermostat_frame = thermostat_frame

        return ant_frame

    def set_windowed(self):
        self.master.geometry('800x480')

    def start_capture(self, source):
        self.vs = cv2.VideoCapture(source)

        sleep(0.5)

        if self.vs.isOpened():
            print("Could not open video device")

        self.vs.set(3, 640)
        self.vs.set(4, 480)

    def stop_capture(self):
        self.vs.release()
        del self.vs

    def video_loop(self):
        if self.stop_camera_signal:
            self.update_camera_frame('', '')
            self.stop_camera_signal = False
            return

        ok, frame = self.vs.read()

        if ok:  # frame captured without any errors
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
            current_image = Image.fromarray(cv2image)  # convert image for PIL
            imgtk = ImageTk.PhotoImage(image=current_image)  # convert image for tkinter

            self.update_camera_frame(current_image, imgtk)

        self.master.after(60, self.video_loop())

    def set_fullscreen(self):
        self.master.overrideredirect(False)
        self.master.attributes('-fullscreen', True)

    def start_camera(self, source):
        if hasattr(self, 'vs'):
            self.stop_camera()

        self.start_capture(source)

        self.video_loop()

    def stop_camera(self):
        self.stop_camera_signal = True
        sleep(0.5)
        if hasattr(self, 'vs'):
            self.stop_capture()

    def start_ant_camera(self):
        self.start_camera(0)

    def stop_ant_camera(self):
        self.stop_camera()

    def start_printer_camera(self):
        self.start_camera(settings.PRINTER_STREAM_URL)

    def stop_printer_camera(self):
        self.stop_camera()

    def start_ant_stream(self):
        sleep(1)

    def stop_ant_stream(self):
        sleep(1)

    def start_ant_lights(self):
        sleep(1)

    def stop_ant_lights(self):
        sleep(1)

    def start_ant_thermostat(self):
        sleep(1)

    def stop_ant_thermostat(self):
        sleep(1)

    def quit(self):
        self.stop_ant_camera()
        self.master.quit()

    def restart(self):
        sleep(1)

    def halt(self):
        sleep(1)

    def mainloop(self):
        self.master.mainloop()
