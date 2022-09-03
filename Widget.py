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

WEEKDAYS = {
    0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday",
    5: "Saturday", 6: "Sunday"
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

        self.days = self.data["daily"]["time"]
        self.max_temps_daily = self.data["daily"]["temperature_2m_max"]
        self.min_temps_daily = self.data["daily"]["temperature_2m_min"]
        self.sunrise_daily = self.data["daily"]["sunrise"]
        self.sunset_daily = self.data["daily"]["sunset"]

        self.draw()
        format_time()

    def draw(self):
        time = format_time()
        index = self.times.index(time)

        # Date:

        # Icon:
        print()
        img = Image.open("resources/sun.jpeg")
        img = img.resize((100, 100), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        lbl_icon = Label(image=photo)
        lbl_icon.image = photo
        lbl_icon.place(x=10, y=10)
        print("Icon: sun.jpeg")

        # WMO:
        wmo = self.wmos[index]
        lbl_wmo = Label(text=WMO[wmo])
        lbl_wmo.place(x=140, y=70)
        print("WMO: " + str(wmo))

        # temp:
        temp = str(self.temps[index]) + " °C"
        lbl_temp = Label(text=temp)
        lbl_temp.place(x=140, y=25)
        print("temp: " + str(temp))

        # max temp:
        max = str(self.max_temps_daily[0]) + " °C"
        lbl_max = Label(text=max)
        lbl_max.place(x=140, y=25)
        print("max: " + str(max))

        # min temp:
        min = str(self.min_temps_daily[0]) + " °C"
        lbl_min= Label(text=min)
        lbl_min.place(x=140, y=25)
        print("min: " + str(min))

        # wind:
        wind = str(self.winds[index]) + " km/h"
        lbl_wind = Label(text=wind)
        lbl_wind.place(x=70, y=120)
        print("wind: " + str(wind))

        # humidity:
        hum = str(self.hums[index]) + " %"
        lbl_hum = Label(text=hum)
        lbl_hum.place(x=10, y=120)
        print("hum: " + str(hum))

        # Hourly + sun raise and set
        print()
        print("Scroll right bar:")
        hourly = ""
        print("Now: " + str(self.temps[index]) + " °C")
        day = 0
        sunrise = self.sunrise_daily[day]
        sunrise = sunrise[len(sunrise) - 5:]
        sunset = self.sunset_daily[day]
        sunset = sunset[len(sunset) - 5:]
        for i in range(index + 1, len(self.times)):
            t = str(self.times[i])
            t = int(t[len(t) - 5:len(t) - 3])
            if t == 0:
                hourly += "\n"
                day += 1
                sunrise = self.sunrise_daily[day]
                sunrise = sunrise[len(sunrise) - 5:]
                sunset = self.sunset_daily[day]
                sunset = sunset[len(sunset) - 5:]
            if t < 10:
                hourly += "0"
            hourly += str(t) + ":00 " + str(self.temps[i]) + " °C, "
            # sunrise:
            if int(sunrise[:2]) == t:
                hourly += "\nSUNRISE: " + sunrise + "\n"
            # sunset:
            if int(sunset[:2]) == t:
                hourly += "\nSUNSET: " + sunset + "\n"
        print(hourly)
        print()

        # forecast for 7 days:
        print()
        print("Scroll down bar:")

        today = datetime.today().weekday() + 1
        daily = ""
        print("Today: " + str(self.min_temps_daily[0]) + " °C, " + str(self.max_temps_daily[0]) + " °C")
        for i in range(1, len(self.days)):
            weekday = WEEKDAYS[today]
            daily += weekday + ": " + str(self.min_temps_daily[i]) + " °C, " + str(self.max_temps_daily[i]) + " °C\n"
            today += 1
            if today == 7:
                today = 0
            i += 1
        print(daily)
        print()

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
