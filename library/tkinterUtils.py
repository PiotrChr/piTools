import tkinter

def createSmallLabel(container, text):
    return tkinter.Label(container, text=text, height=1, font=("Helvetica", 12))

def createMediumLabel(container, text):
    return tkinter.Label(container, text=text, height=2, anchor='nw', font=("Helvetica", 14))