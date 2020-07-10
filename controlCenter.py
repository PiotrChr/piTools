import os
import subprocess
import time
from layout import layout
import argparse


class ControlCenterGUI:
    CURRENT_VERSION = '0.1'
    APP_NAME = 'Control Center'

    def __init__(self):
        self.initializeV4l2()
        self.layout = layout.ControlCenterGUI(self.APP_NAME)
        self.setFullscreen(False)

        parser = argparse.ArgumentParser()
        parser.add_argument("-m", "--mode", help="set mode (f or w)")
        args = parser.parse_args()

        self.setFullscreen(args.mode and args.mode == 'f' and True or False)

    def initializeV4l2(self):
        # Start on arm only
        if os.uname()[4].startswith("arm") and not os.path.exists('/dev/video0'):
            rpistr = "sudo modprobe bcm2835-v4l2"
            p = subprocess.Popen(rpistr, shell=True, preexec_fn=os.setsid)
            time.sleep(1)

    def setFullscreen(self, fullScreen):
        if fullScreen:
            self.layout.setFullscreen()
        else:
            self.layout.setWindowed()

    def quit(self):
        self.layout.stopAntCamera()
        self.layout.quit()

    def start(self):
        self.layout.mainloop()


app = ControlCenterGUI()
app.start()
