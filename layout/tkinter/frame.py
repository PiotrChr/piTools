import tkinter


class Frame(tkinter.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sub_frames = {}
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        if key in self.data:
            return self.data[key]

        return None

    @staticmethod
    def prefix():
        return 'layout_'

    def name(self):
        return self.prefix + self.__name__

    @staticmethod
    def create_name(name):
        return Frame.prefix() + name
