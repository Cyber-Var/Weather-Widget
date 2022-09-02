import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()


class Widget:

    def __init__(self, data):
        self.data = data
        self.draw()
        self.print_data()

    def draw(self):
        root.title("Weather Widget")
        root.geometry('300x300')

        tab_control = ttk.Notebook(root)

        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab1, text="Today")
        tab_control.add(tab2, text="Tomorrow")
        tab_control.pack(expand=1, fill="both")

        style = ttk.Style()
        style.configure('My.TLabel', background='00FF00')
        ttk.Label(tab1, text="Latitude:", style='My.TLabel').grid(column=0, row=0, sticky=W, pady=2)
        ttk.Label(tab1, text=self.data['latitude']).grid(column=1, row=0, sticky=W, pady=2)

        root.mainloop()

    def print_data(self):
        print(self.data['latitude'])
