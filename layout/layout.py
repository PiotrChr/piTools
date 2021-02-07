import tkinter
from layout.view import antFrame, homeFrame, printerFrame, statusFrame, frontDoorFrame, securityFrame
from layout.templating import create_templating


class Layout:
    def __init__(self, title, width, height):
        self.data = {}
        self.master = tkinter.Tk()
        self.master.title(title)
        self.width = width
        self.height = height
        templating = create_templating(width, height)
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
            frontDoorFrame.FrontDoorFrame,
            antFrame.AntFrame,
            printerFrame.PrinterFrame,
            statusFrame.StatusFrame,
            securityFrame.SecurityFrame
        ]

    def set_windowed(self, resolution='800x480'):
        self.master.geometry(resolution)

    def set_fullscreen(self):
        self.master.overrideredirect(False)
        self.master.attributes('-fullscreen', True)

    def open_home(self):
        # print(self.__dict__)
        templating.raise_frame(self[homeFrame.HomeFrame.__name__])

    def update_camera_frame(self, image, imagetk, camera_frame):
        self[camera_frame].left_frame.video_frame.current_image = image
        self[camera_frame].left_frame.video_frame.imgtk = imagetk
        self[camera_frame].left_frame.video_frame.config(image=imagetk)  # show the image

    def mainloop(self):
        self.master.mainloop()

