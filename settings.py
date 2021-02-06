import platform
import os

PRINTER_BASE_URL = 'http://192.168.0.233'
PRINTER_PAGE_URL = 'http://192.168.0.233'
PRINTER_STREAM_URL = 'http://192.168.0.233/webcam/?action=stream'

FRONT_DOOR_BASE_URL = 'http://192.168.0.233'
FRONT_DOOR_STREAM_PATH = '/video_feed'
FRONT_DOOR_STREAM_START_PATH = '/feed_start'
FRONT_DOOR_STREAM_STOP_PATH = '/feed_stop'
FRONT_DOOR_STREAM_STATUS_PATH = '/feed_status'


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
DIMENSIONS = {
    'small': {
        'width': 800,
        'height': 480
    },
    'square': {
        'width': 1280,
        'height': 1024
    },
    'other': {
        'width': 1280,
        'height': 768
    }
}
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

MENU = {
    'status': {
        'title': 'Status'
    },
    'frontDoor': {
        'title': 'Front door'
    },
    'ants': {
        'title': 'Ants'
    },
    '3dprinter': {
        'title': '3D Printer'
    },
    'security': {
        'title': 'Security'
    }
}


def resolution(restype):
    return str(DIMENSIONS[restype]['width']) + 'x' + str(DIMENSIONS[restype]['height'])
