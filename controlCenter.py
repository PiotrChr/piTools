import tkinter
from PIL import Image, ImageTk
from library import httpUtils
from time import sleep
import os
import subprocess
import time
import cv2


class ControlCenterGUI:
    BUTTON_HEIGHT = 10
    BUTTON_WIDTH = 50

    def __init__(self, master):
        self.master = master
        master.title("Control Center")
        self.initializeV4l2()
        self.stopCameraSignal = False

        self.getLayout()

    def startCapture(self):
        self.vs = cv2.VideoCapture(0)
        sleep(0.5)

        if self.vs.isOpened():
            print("Could not open video device")

        self.vs.set(3, 640)
        self.vs.set(4, 480)

    def stopCapture(self):
        if self.vs:
            self.vs.release()
            del self.vs

    def getLayout(self):
        layout = tkinter.Frame(self.master)
        layout.grid()
        layout.mainLabel = tkinter.Label(layout, text="Camera Control").grid(row=0, columnspan=2)

        statusFrame = self.getStatusFrame(layout)
        statusFrame.grid(row=1, column=1)
        layout.statusFrame = statusFrame

        cameraFrameLabel = tkinter.Label(layout)
        cameraFrameLabel.grid(row=2, column=0, padx=4, pady=6)
        layout.cameraFrameLabel = cameraFrameLabel

        layout.antFrame = self.getAntFrame(layout)
        layout.antFrame.grid(row=2, column=1)
        layout.closeButton = tkinter.Button(layout, text="Quit", command=self.quit, width=self.BUTTON_WIDTH * 2,
                                            height=self.BUTTON_HEIGHT).grid(row=4,
                                                                            columnspan=2,
                                                                            padx=5,
                                                                            pady=5)
        self.layout = layout

    def getStatusFrame(self, container):
        statusFrame = tkinter.Frame(container)

        ipLabel = tkinter.Label(statusFrame, text="Ip:")
        ipLabel.grid(row=0, column=0)
        statusFrame.ipLabel = ipLabel

        ipValue = tkinter.Label(statusFrame, text=httpUtils.getHostIp())
        ipValue.grid(row=0, column=1)
        statusFrame.ipValue = ipValue

        hostLabel = tkinter.Label(statusFrame, text="Host:")
        hostLabel.grid(row=1, column=0)
        statusFrame.hostLabel = hostLabel

        hostValue = tkinter.Label(statusFrame, text=httpUtils.getHostName())
        hostValue.grid(row=1, column=1)
        statusFrame.ipValue = hostValue

        return statusFrame

    def getAntFrame(self, container):
        antFrame = tkinter.Frame(container)
        antFrame.startButton = tkinter.Button(antFrame, text="Start Camera", command=self.startCamera,
                                              width=self.BUTTON_WIDTH,
                                              height=self.BUTTON_HEIGHT).grid(row=1, padx=5, pady=5)
        antFrame.stopButton = tkinter.Button(antFrame, text="Stop Camera", command=self.stopCamera,
                                             width=self.BUTTON_WIDTH,
                                             height=self.BUTTON_HEIGHT).grid(row=2, padx=5, pady=5)

        return antFrame

    def videoLoop(self):
        if not hasattr(self.layout, 'antFrame'):
            raise Exception("AntFrame is not initialized")

        if self.stopCameraSignal:
            self.layout.cameraFrameLabel.config(image='')
            self.stopCameraSignal = False
            return

        ok, frame = self.vs.read()
        if ok:  # frame captured without any errors
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
            currentImage = Image.fromarray(cv2image)  # convert image for PIL
            self.layout.cameraFrameLabel.currentImage = currentImage
            imgtk = ImageTk.PhotoImage(image=currentImage)  # convert image for tkinter
            self.layout.cameraFrameLabel.imgtk = imgtk
            self.layout.cameraFrameLabel.config(image=imgtk)  # show the image

        self.master.after(60, self.videoLoop)

    def initializeV4l2(self):
        # Start on arm only
        if os.uname()[4].startswith("arm") and not os.path.exists('/dev/video0'):
            rpistr = "sudo modprobe bcm2835-v4l2"
            p = subprocess.Popen(rpistr, shell=True, preexec_fn=os.setsid)
            time.sleep(1)

    def setFullscreen(self):
        self.master.overrideredirect(False)
        self.master.attributes('-fullscreen', True)

    def startCamera(self):
        if not hasattr(self, 'vs'):
            self.startCapture()

        self.videoLoop()

    def stopCamera(self):
        self.stopCameraSignal = True
        sleep(0.5)
        self.stopCapture()

    def quit(self):
        self.stopCamera()
        self.master.quit()


root = tkinter.Tk()
my_gui = ControlCenterGUI(root)

root.mainloop()
