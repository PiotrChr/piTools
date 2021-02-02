import tkinter


class Frame(tkinter.Frame):

    def __setitem__(self, key, value):
        if not hasattr(self, 'data'):
            self.data = {}

        self.data[key] = value

    def __getitem__(self, item):
        return self.data[item]
