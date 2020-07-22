from layout.templating import templating
from PIL import Image, ImageTk
from time import sleep
import cv2
import settings


class Controller:
    def __init__(self, container, after, quitApp):
        self.container = container
        self.stop_camera_signal = False
        self.after = after
        self.quitApp = quitApp

    def ant_frame(self):
        templating.raise_frame(self.container.AntFrame)

    def home_frame(self):
        templating.raise_frame(self.container.HomeFrame)

    def printer_frame(self):
        templating.raise_frame(self.container.PrinterFrame)

    def status_frame(self):
        templating.raise_frame(self.container.StatusFrame)

    def back(self):
        templating.raise_frame(self.container.HomeFrame)

    @staticmethod
    def update_camera_frame(image, imagetk, camera_frame):
        camera_frame.cameraframe_label.currentImage = image
        camera_frame.cameraframe_label.imgtk = imagetk
        camera_frame.cameraframe_label.config(image=imagetk)  # show the image
        camera_frame.cameraframe_label.config(image=imagetk)  # show the image

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

    def video_loop(self, camera_frame):
        if self.stop_camera_signal:
            self.update_camera_frame('', '', camera_frame)
            self.stop_camera_signal = False
            return

        ok, frame = self.vs.read()

        if ok:  # frame captured without any errors
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
            current_image = Image.fromarray(cv2image)  # convert image for PIL
            imgtk = ImageTk.PhotoImage(image=current_image)  # convert image for tkinter

            self.update_camera_frame(current_image, imgtk, camera_frame)

        self.after(60, self.video_loop(camera_frame))

    def start_camera(self, source, camera_frame):
        if hasattr(self, 'vs'):
            self.stop_camera()

        self.start_capture(source)

        self.video_loop(camera_frame)

    def stop_camera(self):
        self.stop_camera_signal = True
        sleep(0.5)
        if hasattr(self, 'vs'):
            self.stop_capture()

    def start_ant_camera(self):
        self.start_camera(0, self.container.AntFrame.left_frame.video_frame)

    def stop_ant_camera(self):
        self.stop_camera()

    def start_printer_camera(self):
        self.start_camera(settings.PRINTER_STREAM_URL, self.container.AntFrame.left_frame.video_frame)

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
        self.stop_camera()
        self.quitApp()

    def restart(self):
        sleep(1)

    def halt(self):
        sleep(1)
