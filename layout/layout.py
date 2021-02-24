import tkinter
from layout.view import antFrame, homeFrame, printerFrame, statusFrame, frontDoorFrame, securityFrame, utilsFrame
from infrastructure.controller import antController, frontDoorController, homeController, printerController, statusController, securityController, utilsController
from layout.templating import create_templating
from layout.tkinter import frame


class Layout(frame.Frame):
    def __init__(self, title, width, height):
        self.master = tkinter.Tk()
        super().__init__(self.master)
        self.master.title(title)
        self.width = width
        self.height = height
        self.templating = create_templating(width, height)
        self.pack()

        for layout_frame in self.get_frames():
            new_frame = layout_frame[0](
                self,
                layout_frame[1],
                self.templating
            )
            new_frame.grid(row=0, column=0)
            self.set(
                layout_frame[0].__name__,
                new_frame
            )

        utils_frame = self.get_utils_frame()
        utils_frame.grid(row=1, column=0, sticky="snew")
        # utils_frame.pack_propagate(False)
        self.set('utils_frame', utils_frame)

        self.open_home()

    def get_utils_frame(self):
        return utilsFrame.UtilsFrame(
            self,
            utilsController.UtilsController,
            self.templating
        )

    @staticmethod
    def get_frames():
        return [
            [homeFrame.HomeFrame, homeController.HomeController],
            [frontDoorFrame.FrontDoorFrame, frontDoorController.FrontDoorController],
            [antFrame.AntFrame, antController.AntController],
            [printerFrame.PrinterFrame, printerController.PrinterController],
            [statusFrame.StatusFrame, statusController.StatusController],
            [securityFrame.SecurityFrame, securityController.SecurityController]
        ]

    def set_windowed(self, resolution='800x480'):
        self.master.geometry(resolution)

    def set_fullscreen(self):
        self.master.overrideredirect(False)
        self.master.attributes('-fullscreen', True)

    def open_home(self):
        # print(self.__dict__)
        self.templating.raise_frame(
            self.get(homeFrame.HomeFrame.__name__)
        )

    def start_mainloop(self):
        self.master.mainloop()

