import tkinter
from layout.view import antFrame, homeFrame, printerFrame, statusFrame
from layout.templating import templating
from PIL import Image, ImageTk
import cv2
import settings
from library.sysUtils import SysUtils


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
        templating.raise_frame(self[antFrame.AntFrame.__name__])

    def open_home(self):
        # print(self.__dict__)
        templating.raise_frame(self[homeFrame.HomeFrame.__name__])

    def open_printer(self):
        templating.raise_frame(self[printerFrame.PrinterFrame.__name__])

    def open_status(self):
        templating.raise_frame(self[statusFrame.StatusFrame.__name__])

    def back(self):
        templating.raise_frame(self[homeFrame.HomeFrame.__name__])

    def open_printer_page(self):
        self.not_yet_implemented()

    def update_camera_frame(self, image, imagetk, camera_frame):
        self[camera_frame].left_frame.video_frame.current_image = image
        self[camera_frame].left_frame.video_frame.imgtk = imagetk
        self[camera_frame].left_frame.video_frame.config(image=imagetk)  # show the image

    def start_capture(self, source):
        self.vs = cv2.VideoCapture(source)

        self.vs.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.vs.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

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
        else:
            templating.errorbox('Stream error', 'Stream error, quitting')
            self.stop_camera_signal = True

        self.master.after(100, lambda: self.video_loop(camera_frame))

    def start_camera(self, source, camera_frame):
        if hasattr(self, 'vs'):
            self.stop_camera()

        self.start_capture(source)
        self.video_loop(camera_frame)

    def stop_camera(self):
        self.stop_camera_signal = True
        if hasattr(self, 'vs'):
            self.stop_capture()

    def start_ant_camera(self):
        self.start_camera(0, antFrame.AntFrame.__name__)

    def stop_ant_camera(self):
        self.stop_camera()

    def start_printer_camera(self):
        try:
            SysUtils.validate_host(settings.PRINTER_BASE_URL, settings.PRINTER_STREAM_URL)
        except Exception as exception:
            templating.errorbox(message=str(exception))
            return

        self.start_camera(settings.PRINTER_STREAM_URL, printerFrame.PrinterFrame.__name__)

    def stop_printer_camera(self):
        self.stop_camera()

    def start_ant_stream(self):
        self.not_yet_implemented()

    def stop_ant_stream(self):
        self.not_yet_implemented()

    def start_ant_lights(self):
        self.not_yet_implemented()

    def stop_ant_lights(self):
        self.not_yet_implemented()

    def start_ant_thermostat(self):
        self.not_yet_implemented()

    def stop_ant_thermostat(self):
        self.not_yet_implemented()

    def quit(self):
        self.stop_camera()
        self.master.quit()

    def restart(self):
        self.not_yet_implemented()

    def halt(self):
        self.not_yet_implemented()

    def mainloop(self):
        self.master.mainloop()

    @staticmethod
    def not_yet_implemented():
        templating.infobox('Info', 'Not yet implemented')
