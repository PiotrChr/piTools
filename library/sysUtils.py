from library import utils


class SysUtils:

    @staticmethod
    def host_ip():
        return utils.get_host_ip()

    @staticmethod
    def host_name():
        return utils.get_host_name()