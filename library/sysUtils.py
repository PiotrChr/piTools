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
    def ping(host, is_rasp=True):
        timeout = 0.2 if is_rasp else 200
        return True if os.system("ping -c 1 -W " + str(timeout) + " " + host.replace('http://', '')) == 0 else False

    @staticmethod
    def host_up(host):
        return utils.get_response_code(host) == 200

    @staticmethod
    def validate_host(host, url=None, is_rasp=True):
        if not SysUtils.ping(host, is_rasp):
            raise Exception("Host down")

        if url and not SysUtils.host_up(url):
            raise Exception("Host down")
