from settings import MENU


class MenuItem:
    def __init__(self, id, title, action):
        self.id = id
        self.title = title
        self.action = action


menu = [
    MenuItem('status', MENU['status']['title'], 'open_status'),
    MenuItem('security', MENU['security']['title'], 'open_security'),
    MenuItem('frontDoor', MENU['frontDoor']['title'], 'open_front_door'),
    MenuItem('ants', MENU['ants']['title'], 'open_ant'),
    MenuItem('printer', MENU['3dprinter']['title'], 'open_printer'),
]
