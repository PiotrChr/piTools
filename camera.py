import tkinter

from picamera import PiCamera
from fractions import Fraction
from time import sleep


class Camera:
    def __init__(self):
        self.camera = PiCamera(
            framerate=Fraction(1, 6)
        )

    def setLowLightMode(self):
        self.camera.sensor_mode = 3
        self.camera.shutter_speed = 6000000
        self.camera.iso = 800
        sleep(5)
        self.camera.exposure_mode = 'off'

    def setNormalMode(self):
        self.camera.iso = 200
        sleep(5)

    def start(self):
        self.camera.start_preview()

    def stop(self):
        self.camera.stop_preview()


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        self.camera = Camera()
        master.title("A simple GUI")

        self.label = tkinter.Label(master, text="This is our first GUI!")
        self.label.pack()

        self.start_camera_button = tkinter.Button(master, text="Start Camera", command=self.startCamera)
        self.start_camera_button.pack()

        self.stop_camera_button = tkinter.Button(master, text="Stop Camera", command=self.stopCamera)
        self.stop_camera_button.pack()

        self.close_button = tkinter.Button(master, text="Quit", command=self.quit)
        self.close_button.pack()

    def buttonRack(self):
        return [

        ]

    def setLowLightMode(self):
        self.camera.setLowLightMode()

    def setNormalMode(self):
        self.camera.setNormalMode()

    def startCamera(self):
        self.camera.start()
        sleep(10)
        self.camera.stop()

    def stopCamera(self):
        self.camera.stop()

    def quit(self):
        self.stopCamera()
        self.master.quit()


root = tkinter.Tk()
my_gui = MyFirstGUI(root)

root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen', True)

root.mainloop()