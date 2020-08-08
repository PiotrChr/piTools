from library import utils


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
    def host_up(host):
        return utils.get_response_code(host) == 200
