import tkinter
from layout.view import antFrame, homeFrame, printerFrame, statusFrame, frontDoorFrame, securityFrame
from infrastructure.controller import antController, frontDoorController, homeController, printerController
from layout.templating import create_templating


class Layout:
    def __init__(self, title, width, height):
        self.data = {}
        self.master = tkinter.Tk()
        self.master.title(title)
        self.width = width
        self.height = height
        self.templating = create_templating(width, height)
        self.layout = tkinter.Frame()
        self.layout.pack()

        for frame in self.get_frames():
            self[frame[0].__name__] = frame[0](self.layout, frame[1], self.templating)
            self[frame.__name__].grid(row=0, column=0, sticky="nsew")

        self.open_home()

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, item):
        return self.data[item]

    @staticmethod
    def get_frames():
        return [
            [homeFrame.HomeFrame, homeController.HomeController],
            [frontDoorFrame.FrontDoorFrame, frontDoorController.FrontDoorController],
            [antFrame.AntFrame, antController.AntController],
            [printerFrame.PrinterFrame, printerController.PrinterController],
            [statusFrame.StatusFrame, homeController.HomeController],
            [securityFrame.SecurityFrame, homeController.HomeController]
        ]

    def set_windowed(self, resolution='800x480'):
        self.master.geometry(resolution)

    def set_fullscreen(self):
        self.master.overrideredirect(False)
        self.master.attributes('-fullscreen', True)

    def open_home(self):
        # print(self.__dict__)
        self.templating.raise_frame(self[homeFrame.HomeFrame.__name__])

    def mainloop(self):
        self.master.mainloop()

