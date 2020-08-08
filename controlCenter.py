import os
import subprocess
import time
from layout import layout
import argparse
import settings


class ControlCenterGUI:
    CURRENT_VERSION = '0.1'
    APP_NAME = 'Control Center'

    def __init__(self):
        self.initialize_v4l2()
        print(settings.OS)
        parser = argparse.ArgumentParser()
        parser.add_argument("-m", "--mode", help="set mode (f or w)")
        args = parser.parse_args()

        if settings.DEBUG:
            import sys
            print(sys.modules.keys())

        # Init
        self.layout = layout.Layout(self.APP_NAME)
        self.set_mode(args.mode and args.mode == 'f' and True or False)
        self.set_mode(False)

    @staticmethod
    def initialize_v4l2():
        # Start on arm only
        if os.uname()[4].startswith("arm") and not os.path.exists('/dev/video0'):
            rpistr = "sudo modprobe bcm2835-v4l2"
            p = subprocess.Popen(rpistr, shell=True, preexec_fn=os.setsid)
            time.sleep(1)

    def set_mode(self, full_screen):
        if full_screen:
            self.layout.set_fullscreen()
        else:
            self.layout.set_windowed()

    def start(self):
        self.layout.mainloop()


app = ControlCenterGUI()
app.start()
