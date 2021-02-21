import tkinter


class Frame(tkinter.Frame, dict):

    def __setitem__(self, key, value):
        if not key.startswith(self.prefix()):
            self.configure({key: value})
            return

        if not hasattr(self, 'data'):
            self.data = {}

        self.data[key] = value

    def __getitem__(self, key):
        if not key.startswith(self.prefix()):
            return self.cget(key)

        return self.data[key]

    @staticmethod
    def prefix():
        return 'layout_'

    def name(self):
        return self.prefix + self.__name__

    @staticmethod
    def create_name(name):
        return Frame.prefix() + name
