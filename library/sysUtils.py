from library import utils
import os

class SysUtils:

    @staticmethod
    def host_ip():
        return utils.get_host_ip()

    @staticmethod
    def host_name():
        return utils.get_host_name()

    @staticmethod
    def host_device():
        return utils.get_host_device()

    @staticmethod
    def uptime():
        return utils.get_uptime()

    @staticmethod
    def ping(host):
        return True if os.system("ping -c 1 " + host) is 0 else False

    @staticmethod
    def host_up(host):
        responsecode = utils.get_response_code(host)
        return utils.get_response_code(host) == 200
