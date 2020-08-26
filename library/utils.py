import socket
import netifaces as ni
import settings
import psutil
import time
import datetime
from urllib import request


def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)


def get_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    delta = datetime.timedelta(seconds=uptime_seconds)

    return strfdelta(delta, '{days} days {hours} hours {minutes} m {seconds} s')


def get_host_device():
    device = None

    for net_device in settings.NET_DEVICES:
        if net_device_on(net_device):
            device = net_device

    return device


def net_device_on(net_device):
    try:
        ni.ifaddresses(net_device)
        return True
    except:
        return False


def get_host_ip():
    device = get_host_device()

    if not device:
        raise Exception("Cannot find net device")

    return ni.ifaddresses(device)[ni.AF_INET][0]['addr']


def get_host_name():
    try:
        return socket.gethostname()
    except:
        print("Unable to get Hostname")


def get_response_code(host):
    response = request.urlopen(host)
    return response.getcode()
