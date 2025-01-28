from .calculator import Calculator
from tkinter import *
from tkinter import ttk

class GUI_Application():
    def __init__(self, calc: Calculator):
        self.calc = calc
        self.window = Tk()
        # print(ttk.Style().theme_names())
        # ttk.Style().theme_use("classic")
        self.window.title("Anomaly")
        self.label = ttk.Label(text = "Hello World")
        self.label.pack()




