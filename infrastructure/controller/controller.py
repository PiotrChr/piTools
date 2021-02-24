from infrastructure.http.client import Client
from layout.view.homeFrame import HomeFrame
import os
from PIL import Image, ImageTk
import cv2


class Controller:
    def __init__(self, layout):
        self.stop_camera_signal = False
        self.templating = None
        self.layout = layout
        self.http_client = Client()

    def set_templating(self, templating):
        self.templating = templating

    def open_frame(self, frame):
        self.templating.raise_frame(frame)

    def start_camera(self, source, camera_frame):
        if hasattr(self, 'vs'):
            self.stop_camera()

        self.start_capture(source)
        self.video_loop(camera_frame, self.update_camera_frame)

    def stop_camera(self):
        self.stop_camera_signal = True
        if hasattr(self, 'vs'):
            self.stop_capture()

    def start_capture(self, source):
        self.vs = cv2.VideoCapture(source)

        self.vs.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.vs.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def stop_capture(self):
        self.vs.release()
        del self.vs

    def not_yet_implemented(self):
        self.templating.infobox('Info', 'Not yet implemented')

    def quit(self):
        self.stop_camera()
        self.layout.master.quit()

    def restart(self):
        if self.templating.promptbox(None, 'Are you sure?'):
            os.system('reboot')

    def halt(self):
        if self.templating.promptbox(None, 'Are you sure?'):
            os.system('halt')

    def video_loop(self, camera_frame, update_camera_frame):
        if self.stop_camera_signal:
            update_camera_frame('', '', camera_frame)
            self.stop_camera_signal = False
            return

        ok, frame = self.vs.read()
        if ok:  # frame captured without any errors
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
            current_image = Image.fromarray(cv2image)  # convert image for PIL
            imgtk = ImageTk.PhotoImage(image=current_image)  # convert image for tkinter

            self.layout.master(current_image, imgtk, camera_frame)
        else:
            self.templating.errorbox('Stream error', 'Stream error, quitting')
            self.stop_camera_signal = True

        self.layout.master.after(100, lambda: self.video_loop(camera_frame))

    def back(self):
        self.templating.raise_frame(self.layout.get(HomeFrame.__name__))

    def update_camera_frame(self, image, imagetk, camera_frame):
        self.layout[camera_frame].left_frame.video_frame.current_image = image
        self.layout[camera_frame].left_frame.video_frame.imgtk = imagetk
        self.layout[camera_frame].left_frame.video_frame.config(image=imagetk)  # show the image
