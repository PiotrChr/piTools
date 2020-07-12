import tkinter


def create_small_label(container, text):
    return tkinter.Label(container, text=text, height=1, font=("Helvetica", 10))


def create_medium_label(container, text):
    return tkinter.Label(container, text=text, height=1, anchor='e', font=("Helvetica", 12))


def raise_frame(frame):
    frame.tkraise()
