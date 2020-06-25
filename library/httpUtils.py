import socket

def getHostIp():
    try:
        host_name = socket.gethostname()
        return socket.gethostbyname(host_name)
    except:
        print("Unable to get IP")


def getHostName():
    try:
        return socket.gethostname()
    except:
        print("Unable to get Hostname")