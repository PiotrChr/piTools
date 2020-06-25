import tkinter
from PIL import Image, ImageTk
from library import httpUtils
from time import sleep
import os
import subprocess
import time
import cv2


class ControlCenterGUI:
    BAR_BUTTON_HEIGHT = 2
    BAR_BUTTON_WIDTH = 15

    def __init__(self, master):
        self.master = master
        self.setFullscreen()
        master.title("Control Center")
        self.initializeV4l2()
        self.stopCameraSignal = False

        self.getLayout()

    def startCapture(self):
        self.vs = cv2.VideoCapture(0)
        sleep(0.5)

        if self.vs.isOpened():
            print("Could not open video device")

        self.vs.set(3, 320)
        self.vs.set(4, 240)

    def stopCapture(self):
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
        layout.closeButton = tkinter.Button(layout, text="Quit", command=self.quit, width=self.BAR_BUTTON_WIDTH * 2,
                                            height=self.BAR_BUTTON_HEIGHT).grid(row=4,
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

    def getStatusSection(self, container):
        statusSection = tkinter.Frame(container)

        statusFrame = self.getStatusFrame(statusSection)
        statusFrame.grid(row=0)
        statusSection.statusFrame = statusFrame

        quitButton = tkinter.Button(statusSection, text="Quit", command=self.quit,
                                    width=self.BAR_BUTTON_WIDTH,
                                    height=self.BAR_BUTTON_WIDTH)
        quitButton.grid(row=1)
        statusSection.quitButton = quitButton

        restartButton = tkinter.Button(statusSection, text="Restart", command=self.restart,
                                       width=self.BAR_BUTTON_WIDTH,
                                       height=self.BAR_BUTTON_WIDTH)
        restartButton.grid(row=2)
        statusSection.restartButton = restartButton

        haltButton = tkinter.Button(statusSection, text="Halt", command=self.halt,
                                    width=self.BAR_BUTTON_WIDTH,
                                    height=self.BAR_BUTTON_WIDTH)
        statusSection.grid(row=3)
        statusSection.haltButton = haltButton

        return statusSection

    def getRightBar(self, container):
        rightBar = tkinter.Frame(container)

        statusSection = self.getStatusSection(rightBar)
        rightBar.statusSection = statusSection

        antSection = self.getAntSection(rightBar)
        rightBar.antSection = antSection

        printerSection = self.getPrinterSection(rightBar)
        rightBar.printerSection = printerSection

    def getPrinterSection(self, container):

    def getAntSection(self, container):
        antFrame = tkinter.Frame(container)

        cameraLabel = tkinter.Label(text="Camera")
        cameraLabel.grid(row=0, columnspan=2)
        antFrame.cameraLabel = cameraLabel

        cameraStartButton = tkinter.Button(antFrame, text="Start", command=self.startAntCamera,
                                           width=self.BAR_BUTTON_WIDTH,
                                           height=self.BAR_BUTTON_HEIGHT)
        cameraStartButton.grid(row=1, column=0)
        antFrame.cameraStartButton = cameraStartButton

        cameraStopButton = tkinter.Button(antFrame, text="Stop", command=self.stopAntCamera,
                                          width=self.BAR_BUTTON_WIDTH,
                                          height=self.BAR_BUTTON_HEIGHT)
        cameraStopButton.grid(row=1, column=1)
        antFrame.cameraStopButton = cameraStopButton

        streamLabel = tkinter.Label(text="Stream")
        streamLabel.grid(row=2, columnspan=2)
        antFrame.streamLabel = streamLabel

        streamStartButton = tkinter.Button(antFrame, text="Start", command=self.startAntStream,
                                           width=self.BAR_BUTTON_WIDTH,
                                           height=self.BAR_BUTTON_HEIGHT)
        streamStartButton.grid(row=3, column=0)
        antFrame.streamStrartButton = streamStartButton

        streamStopButton = tkinter.Button(antFrame, text="Stop", command=self.stopAntStream,
                                          width=self.BAR_BUTTON_WIDTH,
                                          height=self.BAR_BUTTON_HEIGHT)
        streamStopButton.grid(row=3, column=1)
        antFrame.streamStopButton = streamStopButton

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

    def startAntCamera(self):
        if not hasattr(self, 'vs'):
            self.startCapture()

        self.videoLoop()

    def stopAntCamera(self):
        self.stopCameraSignal = True
        sleep(0.5)
        if hasattr(self, 'vs'):
            self.stopCapture()

    def startAntStream(self):
        sleep(1)

    def stopAntStream(self):
        sleep(1)

    def quit(self):
        self.stopAntCamera()
        self.master.quit()

    def restart(self):
        sleep(1)

    def halt(self):
        sleep(1)


root = tkinter.Tk()
my_gui = ControlCenterGUI(root)

root.mainloop()
