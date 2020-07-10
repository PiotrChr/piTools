import tkinter
from PIL import Image, ImageTk
from library import httpUtils, tkinterUtils
from time import sleep
import cv2
import sys, getopt
import settings

class ControlCenterGUI:
    BAR_BUTTON_HEIGHT = 2
    BAR_BUTTON_WIDTH = 7

    BUTTON_TEXT_ON = 'Start'
    BUTTON_TEXT_OFF = 'Stop'

    def __init__(self, title):
        self.master = tkinter.Tk()
        self.master.title(title)
        self.stopCameraSignal = False
        self.layout = self.getLayout()

        print('Argument List:', str(sys.argv))

    # def getFrames
    #     return [
    #
    #     ]

    def getLayout(self):
        layout = tkinter.Frame(self.master)
        layout.pack(fill='both', expand=True)

        cameraFrameLabel = tkinter.Label(layout)
        cameraFrameLabel.pack(side='left', fill='y', expand=False)
        layout.cameraFrameLabel = cameraFrameLabel

        rightBar = self.getRightBar(layout)
        rightBar.pack(side='right', fill='y', padx=5, pady=5)
        layout.rightBar = rightBar

        return layout

    def updateCameraFrame(self, image, imagetk):
        self.layout.cameraFrameLabel.currentImage = image
        self.layout.cameraFrameLabel.imgtk = imagetk
        self.layout.cameraFrameLabel.config(image=imagetk)  # show the image
        self.layout.cameraFrameLabel.config(image=imagetk)  # show the image

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

        statusButton = tkinter.Button(statusSection, text="Status", command=self.quit,
                                      width=self.BAR_BUTTON_WIDTH,
                                      height=self.BAR_BUTTON_HEIGHT)
        statusButton.grid(row=0, column=0)
        statusSection.statusButton = statusButton

        quitButton = tkinter.Button(statusSection, text="Quit", command=self.quit,
                                    width=self.BAR_BUTTON_WIDTH,
                                    height=self.BAR_BUTTON_HEIGHT)
        quitButton.grid(row=0, column=1)
        statusSection.quitButton = quitButton

        restartButton = tkinter.Button(statusSection, text="Restart", command=self.restart,
                                       width=self.BAR_BUTTON_WIDTH,
                                       height=self.BAR_BUTTON_HEIGHT)
        restartButton.grid(row=1, column=0)
        statusSection.restartButton = restartButton

        haltButton = tkinter.Button(statusSection, text="Halt", command=self.halt,
                                    width=self.BAR_BUTTON_WIDTH,
                                    height=self.BAR_BUTTON_HEIGHT)
        haltButton.grid(row=1, column=1)
        statusSection.haltButton = haltButton

        return statusSection

    def getRightBar(self, container):
        rightBar = tkinter.Frame(container)

        statusSection = self.getStatusSection(rightBar)
        statusSection.grid(row=0)
        rightBar.statusSection = statusSection

        antSection = self.getAntSection(rightBar)
        antSection.grid(row=1)
        rightBar.antSection = antSection

        printerSection = self.getPrinterSection(rightBar)
        printerSection.grid(row=2)
        rightBar.printerSection = printerSection

        return rightBar

    def getPrinterSection(self, container):
        printerFrame = tkinter.Frame(container)

        frameLabel = tkinterUtils.createMediumLabel(printerFrame, "3D printer Control")
        frameLabel.grid(row=0, columnspan=2, sticky='w')
        printerFrame.frameLabel = frameLabel

        # # Printer Page
        # printerPageButton = tkinter.Button(printerFrame, text='Open printer page', command=self.startAntCamera,
        #                                    width=self.BAR_BUTTON_WIDTH * 2,
        #                                    height=self.BAR_BUTTON_HEIGHT)
        # printerPageButton.grid(row=1, columnspan=2)
        # printerFrame.cameraStartButton = printerPageButton

        # Printer Camera
        cameraLabel = tkinterUtils.createSmallLabel(printerFrame, "Camera")
        cameraLabel.grid(row=1, columnspan=2)
        printerFrame.cameraLabel = cameraLabel

        cameraStartButton = tkinter.Button(printerFrame, text=self.BUTTON_TEXT_ON, command=self.startPrinterCamera,
                                           width=self.BAR_BUTTON_WIDTH,
                                           height=self.BAR_BUTTON_HEIGHT)
        cameraStartButton.grid(row=2, column=0)
        printerFrame.cameraStartButton = cameraStartButton

        cameraStopButton = tkinter.Button(printerFrame, text=self.BUTTON_TEXT_OFF, command=self.stopPrinterCamera,
                                          width=self.BAR_BUTTON_WIDTH,
                                          height=self.BAR_BUTTON_HEIGHT)
        cameraStopButton.grid(row=2, column=1)
        printerFrame.cameraStopButton = cameraStopButton

        return printerFrame

    def getAntSection(self, container):
        antFrame = tkinter.Frame(container)

        frameLabel = tkinterUtils.createMediumLabel(antFrame, text="Ant Control")
        frameLabel.grid(row=0, columnspan=2, sticky='w')
        antFrame.frameLabel = frameLabel

        # Camera
        cameraLabel = tkinterUtils.createSmallLabel(antFrame, text="Camera")
        cameraLabel.grid(row=1, columnspan=2, sticky='w')
        antFrame.cameraLabel = cameraLabel

        cameraStartButton = tkinter.Button(antFrame, text=self.BUTTON_TEXT_ON, command=self.startAntCamera,
                                           width=self.BAR_BUTTON_WIDTH,
                                           height=self.BAR_BUTTON_HEIGHT)
        cameraStartButton.grid(row=2, column=0, sticky='w')
        antFrame.cameraStartButton = cameraStartButton

        cameraStopButton = tkinter.Button(antFrame, text=self.BUTTON_TEXT_OFF, command=self.stopAntCamera,
                                          width=self.BAR_BUTTON_WIDTH,
                                          height=self.BAR_BUTTON_HEIGHT)
        cameraStopButton.grid(row=2, column=1)
        antFrame.cameraStopButton = cameraStopButton

        # Stream
        streamLabel = tkinterUtils.createSmallLabel(antFrame, text="Stream")
        streamLabel.grid(row=3, columnspan=2, sticky='w')
        antFrame.streamLabel = streamLabel

        streamStartButton = tkinter.Button(antFrame, text=self.BUTTON_TEXT_ON, command=self.startAntStream,
                                           width=self.BAR_BUTTON_WIDTH,
                                           height=self.BAR_BUTTON_HEIGHT)
        streamStartButton.grid(row=4, column=0)
        antFrame.streamStartButton = streamStartButton

        streamStopButton = tkinter.Button(antFrame, text=self.BUTTON_TEXT_OFF, command=self.stopAntStream,
                                          width=self.BAR_BUTTON_WIDTH,
                                          height=self.BAR_BUTTON_HEIGHT)
        streamStopButton.grid(row=4, column=1)
        antFrame.streamStopButton = streamStopButton

        # Lights
        lightsLabel = tkinterUtils.createSmallLabel(antFrame, text="Lights")
        lightsLabel.grid(row=5, columnspan=2, sticky='w')
        antFrame.lightsLabel = lightsLabel

        lightsStartButton = tkinter.Button(antFrame, text=self.BUTTON_TEXT_ON, command=self.startLights,
                                           width=self.BAR_BUTTON_WIDTH,
                                           height=self.BAR_BUTTON_HEIGHT)
        lightsStartButton.grid(row=6, column=0)
        antFrame.lightsStartButton = lightsStartButton

        lightsStopButton = tkinter.Button(antFrame, text=self.BUTTON_TEXT_OFF, command=self.stopLights,
                                          width=self.BAR_BUTTON_WIDTH,
                                          height=self.BAR_BUTTON_HEIGHT)
        lightsStopButton.grid(row=6, column=1)
        antFrame.lightsStopButton = lightsStopButton

        # Thermostat
        thermostatLabel = tkinterUtils.createSmallLabel(antFrame, text="Thermostat")
        thermostatLabel.grid(row=7, columnspan=2, sticky='w')
        antFrame.thermostatLabel = thermostatLabel

        thermostatStartButton = tkinter.Button(antFrame, text=self.BUTTON_TEXT_ON, command=self.startThermostat,
                                               width=self.BAR_BUTTON_WIDTH,
                                               height=self.BAR_BUTTON_HEIGHT)
        thermostatStartButton.grid(row=8, column=0)
        antFrame.thermostatStartButton = thermostatStartButton

        thermostatStopButton = tkinter.Button(antFrame, text=self.BUTTON_TEXT_OFF, command=self.stopThermostat,
                                              width=self.BAR_BUTTON_WIDTH,
                                              height=self.BAR_BUTTON_HEIGHT)
        thermostatStopButton.grid(row=8, column=1)
        antFrame.thermostatStopButton = thermostatStopButton

        return antFrame

    def setWindowed(self):
        self.master.geometry('800x480')

    def startCapture(self, source):
        self.vs = cv2.VideoCapture(source)

        sleep(0.5)

        if self.vs.isOpened():
            print("Could not open video device")

        self.vs.set(3, 640)
        self.vs.set(4, 480)

    def stopCapture(self):
        self.vs.release()
        del self.vs

    def videoLoop(self):
        if self.stopCameraSignal:
            self.updateCameraFrame('', '')
            self.stopCameraSignal = False
            return

        ok, frame = self.vs.read()

        if ok:  # frame captured without any errors
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
            currentImage = Image.fromarray(cv2image)  # convert image for PIL
            imgtk = ImageTk.PhotoImage(image=currentImage)  # convert image for tkinter

            self.updateCameraFrame(currentImage, imgtk)

        self.master.after(60, self.videoLoop)

    def setFullscreen(self):
        self.master.overrideredirect(False)
        self.master.attributes('-fullscreen', True)

    def startCamera(self, source):
        if hasattr(self, 'vs'):
            self.stopCamera()

        self.startCapture(source)

        self.videoLoop()

    def stopCamera(self):
        self.stopCameraSignal = True
        sleep(0.5)
        if hasattr(self, 'vs'):
            self.stopCapture()

    def startAntCamera(self):
        self.startCamera(0)

    def stopAntCamera(self):
        self.stopCamera()

    def startPrinterCamera(self):
        self.startCamera(settings.PRINTER_STREAM_URL)

    def stopPrinterCamera(self):
        self.stopCamera()

    def startAntStream(self):
        sleep(1)

    def stopAntStream(self):
        sleep(1)

    def startLights(self):
        sleep(1)

    def stopLights(self):
        sleep(1)

    def startThermostat(self):
        sleep(1)

    def stopThermostat(self):
        sleep(1)

    def quit(self):
        self.stopAntCamera()
        self.master.quit()

    def restart(self):
        sleep(1)

    def halt(self):
        sleep(1)

    def mainloop(self):
        self.master.mainloop()
