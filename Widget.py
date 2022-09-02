import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime

root = tk.Tk()
root.title("Weather Widget")
root.geometry('300x250')
root.configure(bg='#83C4CE')

WMO = {
    0: "Clear sky",
    1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Depositing rime fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense intensity drizzle",
    56: "Light freezing drizzle", 57: "Dense intensity freezing drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    66: "Light freezing rain", 67: "Heavy intensity freezing rain",
    71: "Slight snow fall", 73: "Moderate snow fall", 75: "Heavy intensity snow fall",
    77: "Snow grains",
    80: "Slight rain showers", 81: "Moderate rain showers", 82: "Heavy intensity rain showers",
    85: "Slight snow showers", 86: "Heavy intensity snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail"
}


def format_time():
    current = datetime.now()
    iso = current.isoformat()
    formatted = iso.split('.', 1)[0]
    formatted = formatted[:len(formatted) - 5] + "00"
    return formatted


class Widget:

    def __init__(self, data):
        self.data = data
        self.wmos = self.data["hourly"]["weathercode"]
        self.times = self.data["hourly"]["time"]
        self.temps = self.data["hourly"]["temperature_2m"]
        self.hums = self.data["hourly"]["relativehumidity_2m"]
        self.winds = self.data["hourly"]["windspeed_10m"]

        self.draw()
        self.print_data()
        format_time()

    def draw(self):
        time = format_time()
        index = self.times.index(time)

        # Icon:
        img = Image.open("resources/sun.jpeg")
        img = img.resize((100, 100), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        lbl_icon = Label(image=photo)
        lbl_icon.image = photo
        lbl_icon.place(x=10, y=10)

        # WMO:
        wmo = self.wmos[index]
        lbl_wmo = Label(text=WMO[wmo])
        lbl_wmo.place(x=140, y=70)

        # temp:
        temp = str(self.temps[index]) + "°C"
        lbl_temp = Label(text=temp)
        lbl_temp.place(x=140, y=25)

        # wind:
        wind = str(self.winds[index]) + "m/s"
        lbl_wind = Label(text=wind)
        lbl_wind.place(x=70, y=120)

        # humidity:
        hum = str(self.hums[index]) + "%"
        lbl_hum = Label(text=hum)
        lbl_hum.place(x=10, y=120)

        # forecast:

        root.mainloop()

    def print_data(self):
        print(self.data)


'''
from tkinter import ttk

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
'''
