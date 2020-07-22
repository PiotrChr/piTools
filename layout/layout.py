import tkinter
from layout import view, templating, controller as layout_controller


class Layout:
    def __init__(self, title):
        self.master = tkinter.Tk()
        self.master.title(title)

        self.layout = tkinter.Frame(self.master)

        controller = layout_controller.Controller(self.layout, self.master.after, self.master.quit())

        for Frame in self.get_frames():
            self.layout[Frame.__name__] = Frame(self.layout, controller)

    @staticmethod
    def get_frames():
        return [
            view.homeFrame.HomeFrame,
            view.antFrame.AntFrame,
            view.printerFrame.PrinterFrame,
            view.statusFrame.StatusFrame
        ]

    def set_windowed(self):
        self.master.geometry('800x480')

    def set_fullscreen(self):
        self.master.overrideredirect(False)
        self.master.attributes('-fullscreen', True)

    def mainloop(self):
        self.master.mainloop()
