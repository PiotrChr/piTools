import socket


def get_host_ip():
    try:
        host_name = socket.gethostname()
        return socket.gethostbyname(host_name)
    except:
        print("Unable to get IP")


def get_host_name():
    try:
        return socket.gethostname()
    except:
        print("Unable to get Hostname")
