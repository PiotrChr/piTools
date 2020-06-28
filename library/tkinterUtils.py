import tkinter

def createSmallLabel(container, text):
    return tkinter.Label(container, text=text, height=1, font=("Helvetica", 10))

def createMediumLabel(container, text):
    return tkinter.Label(container, text=text, height=1, anchor='e', font=("Helvetica", 12))