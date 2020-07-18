import tkinter
from PIL import Image, ImageTk
from library import httpUtils, tkinterUtils
from time import sleep
import cv2
import settings

from layout import view
from layout import templating


class ControlCenterGUI:
    BAR_BUTTON_HEIGHT = 2
    BAR_BUTTON_WIDTH = 7

    BUTTON_TEXT_ON = 'Start'
    BUTTON_TEXT_OFF = 'Stop'

    def __init__(self, title):
        self.master = tkinter.Tk()
        self.master.title(title)
        self.stop_camera_signal = False

        self.layout = self.get_layout()

        for Frame in self.get_frames():
            self.layout[Frame.__name__] = Frame(self.layout)

    def get_frames(self):
        return [
            view.homeFrame,
            view.antFrame,
            view.printerFrame,
            view.statusFrame
        ]

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
