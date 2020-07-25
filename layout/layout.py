import tkinter
from layout.view import antFrame, homeFrame, printerFrame, statusFrame
from layout.templating import templating
from PIL import Image, ImageTk
from time import sleep
import cv2
import settings


class Layout:
    def __init__(self, title):
        self.data = {}
        self.master = tkinter.Tk()
        self.master.title(title)
        self.stop_camera_signal = False

        self.layout = tkinter.Frame()
        self.layout.pack()

        for Frame in self.get_frames():
            self[Frame.__name__] = Frame(self.layout, self)
            self[Frame.__name__].grid(row=0, column=0, sticky="nsew")

        self.open_home()

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, item):
        return self.data[item]

    @staticmethod
    def get_frames():
        return [
            homeFrame.HomeFrame,
            antFrame.AntFrame,
            printerFrame.PrinterFrame,
            statusFrame.StatusFrame
        ]

    def set_windowed(self):
        self.master.geometry('800x480')

    def set_fullscreen(self):
        self.master.overrideredirect(False)
        self.master.attributes('-fullscreen', True)

    def open_ant(self):
        templating.raise_frame(self['AntFrame'])

    def open_home(self):
        print(self.__dict__)
        templating.raise_frame(self['HomeFrame'])

    def open_printer(self):
        templating.raise_frame(self['PrinterFrame'])

    def open_status(self):
        templating.raise_frame(self['StatusFrame'])

    def back(self):
        templating.raise_frame(self['HomeFrame'])

    def open_printer_page(self):
        sleep(0.5)

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

        self.master.after(60, self.video_loop(camera_frame))

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
        self.start_camera(0, self['AntFrame'].left_frame.video_frame)

    def stop_ant_camera(self):
        self.stop_camera()

    def start_printer_camera(self):
        self.start_camera(settings.PRINTER_STREAM_URL, self.data['PrinterFrame'].left_frame.video_frame)

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
        self.master.quit()

    def restart(self):
        sleep(1)

    def halt(self):
        sleep(1)

    def mainloop(self):
        self.master.mainloop()

