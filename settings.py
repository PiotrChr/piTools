import platform
import os

PRINTER_BASE_URL = 'http://192.168.0.233'
PRINTER_PAGE_URL = 'http://192.168.0.233'
PRINTER_STREAM_URL = 'http://192.168.0.233/webcam/?action=stream'

NET_DEVICES = ['eth0', 'en0', 'wlan0']

LAYOUT_TEXT_OFF = 'Off'
LAYOUT_TEXT_ON = 'On'
BUTTON_TEXT_BACK = 'Back'
BUTTON_TEXT_REFRESH = 'Refresh'
LAYOUT_BUTTON_WIDTH = 20
LAYOUT_BUTTON_HEIGHT = 2
LAYOUT_FONT_SIZE = 10
LAYOUT_BIG_FONT_SIZE = 12
LAYOUT_SMALL_FONT_SIZE = 8
LAYOUT_FONT_FAMILY = 'Helvetica'
LAYOUT_LABEL_HEIGHT = 1
LAYOUT_FRAME_WIDTH = 800
LAYOUT_FRAME_HEIGHT = 500
LAYOUT_FRAME_LEFT_RIGHT_RATIO = 0.72
DEBUG = True

OS = platform.system()
IS_OSX = platform.system() == 'Darwin'
IS_RASP = os.uname()[4].startswith("arm")

COLOR = {
    'lightgreen': '#b5ff8c',
    'lightred': '#ff8c8c'
}