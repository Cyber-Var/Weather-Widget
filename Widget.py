import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime

width = 300
height = 500

root = tk.Tk()
root.title("Weather Widget")
root.geometry(str(width) + "x" + str(height))

frame = Frame(root)
frame.pack()

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

    def __init__(self, data, city):
        self.data = data
        self.city = city

        self.wmos = self.data["hourly"]["weathercode"]
        self.times = self.data["hourly"]["time"]
        self.temps = self.data["hourly"]["temperature_2m"]
        self.hums = self.data["hourly"]["relativehumidity_2m"]
        self.winds = self.data["hourly"]["windspeed_10m"]
        self.precs = self.data["hourly"]["precipitation"]

        self.days = self.data["daily"]["time"]
        self.max_temps_daily = self.data["daily"]["temperature_2m_max"]
        self.min_temps_daily = self.data["daily"]["temperature_2m_min"]
        self.sunrise_daily = self.data["daily"]["sunrise"]
        self.sunset_daily = self.data["daily"]["sunset"]

        self.time = format_time()
        self.index = self.times.index(self.time)

        self.draw()
        format_time()

    def draw(self):
        # Icon:
        img = Image.open("resources/sun.jpeg")
        img = img.resize((70, 70), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        # WMO:
        wmo = self.wmos[self.index]
        # temp:
        temp = str(self.temps[self.index]) + " °C"
        # max and min temp:
        max_min = "max.: " + str(self.max_temps_daily[0]) + " °C" + ", min.: " + str(self.min_temps_daily[0]) + " °C"

        # Main Frame:

        top_frame = Frame(frame, width=width, height=200)
        top_frame.pack(side=TOP)

        lbl_icon = Label(top_frame, image=photo)
        lbl_city = Label(top_frame, text=self.city)
        lbl_temp = Label(top_frame, text=temp)
        lbl_wmo = Label(top_frame, text=WMO[wmo])
        lbl_max_min = Label(top_frame, text=max_min)

        lbl_icon.pack(side=TOP)
        lbl_city.pack(side=TOP)
        lbl_temp.pack(side=TOP)
        lbl_wmo.pack(side=TOP)
        lbl_max_min.pack(side=TOP)

        # Horizontal scroll:

        hor_scroll_frame = Frame(frame, highlightbackground="black", highlightthickness=1)
        hor_scroll_frame.pack(side=TOP, padx=1)

        hor_scroll = Scrollbar(hor_scroll_frame, orient='horizontal')
        hor_scroll.pack(side=TOP, fill='x')

        hor_text = Text(hor_scroll_frame, wrap=NONE, xscrollcommand=hor_scroll.set, height=8)
        hor_text.pack(side=TOP)

        time_now = str(self.times[self.index])
        time_now = int(time_now[len(time_now) - 5:len(time_now) - 3])

        sunrise_today = self.sunrise_daily[0]
        sunrise_today = sunrise_today[len(sunrise_today) - 5:]
        s_t_int = int(sunrise_today[len(sunrise_today) - 5:len(sunrise_today) - 3])
        sunrise_tmrw = self.sunrise_daily[1]
        sunrise_tmrw = sunrise_tmrw[len(sunrise_tmrw) - 5:]
        s_tm_int = int(sunrise_tmrw[len(sunrise_tmrw) - 5:len(sunrise_tmrw) - 3])

        sunset_today = self.sunset_daily[0]
        sunset_today = sunset_today[len(sunset_today) - 5:]
        print(sunset_today)
        su_t_int = int(sunset_today[len(sunset_today) - 5:len(sunset_today) - 3])
        print(su_t_int)
        sunset_tmrw = self.sunset_daily[1]
        sunset_tmrw = sunset_tmrw[len(sunset_tmrw) - 5:]
        su_tm_int = int(sunset_tmrw[len(sunset_tmrw) - 5:len(sunset_tmrw) - 3])

        sunrise = s_t_int
        sunrise_time = sunrise_today
        sunset = su_t_int
        sunset_time = sunset_today
        if time_now > s_t_int:
            sunrise = s_tm_int
            sunrise_time = sunrise_tmrw
        if time_now > su_t_int:
            sunset = su_tm_int
            sunset_time = sunset_tmrw
        print(sunset_time)

        str_now = "{0:^10}".format("Now")
        hor_text.insert(END, str_now)
        for i in range(self.index + 1, self.index + 24):
            t = str(self.times[i])
            t = int(t[len(t) - 5:len(t) - 3])
            str_time = "{0:^10}".format(str(t) + ":00 ")
            hor_text.insert(END, str_time)
            if sunrise == t:
                str_sunrise = "{0:^10}".format(sunrise_time)
                hor_text.insert(END, str_sunrise)
            if sunset == t:
                str_sunset = "{0:^10}".format(sunset_time)
                hor_text.insert(END, str_sunset)
        hor_text.insert(END, "\n")

        hor_text.image_create(END, image=photo)
        for i in range(self.index + 1, self.index + 24):
            t = str(self.times[i])
            t = int(t[len(t) - 5:len(t) - 3])
            hor_text.image_create(END, image=photo)
            if sunrise == t:
                hor_text.image_create(END, image=photo)
            if sunset == t:
                hor_text.image_create(END, image=photo)
        hor_text.insert(END, "\n")

        t = round(int(self.temps[self.index] or 0))
        str_temp = "{0:^10}".format(str(t) + "°C")
        hor_text.insert(END, str_temp)
        for i in range(self.index + 1, self.index + 24):
            t = str(self.times[i])
            t = int(t[len(t) - 5:len(t) - 3])
            te = round(int(self.temps[i] or 0))
            str_temp = "{0:^10}".format(str(te) + "°C")
            hor_text.insert(END, str_temp)
            if sunrise == t:
                str_sunrise = "{0:^10}".format("Sunrise")
                hor_text.insert(END, str_sunrise)
            if sunset == t:
                str_sunset = "{0:^10}".format("Sunset")
                hor_text.insert(END, str_sunset)

        hor_text.config(state=DISABLED)
        hor_scroll.config(command=hor_text.xview)

        # Vertical scroll:

        ver_scroll_frame = Frame(frame, highlightbackground="black", highlightthickness=1)
        ver_scroll_frame.pack(side=TOP, padx=1)

        ver_scroll = Scrollbar(ver_scroll_frame, orient='vertical')
        ver_scroll.pack(side=RIGHT, fill='y')

        ver_text = Text(ver_scroll_frame, wrap=NONE, borderwidth=1, yscrollcommand=ver_scroll.set, height=5)
        ver_text.pack(side=TOP)

        ver_text.tag_config('cold', foreground='#ADD8E6')
        ver_text.tag_config('hot', foreground='#F7B98F')

        str_now = "   " + "{0:^10}".format("Today")
        ver_text.insert(END, str_now)

        str_min = str(round(int(self.min_temps_daily[0] or 0))) + "°C"
        str_min = "{0:^7}".format(str_min)
        ver_text.insert(END, str_min, 'cold')

        img1 = Image.open("resources/coldtohot.jpeg")
        img1 = img1.resize((70, 10), Image.ANTIALIAS)
        photo1 = ImageTk.PhotoImage(img1)
        ver_text.image_create(END, image=photo1)

        str_max = str(round(int(self.max_temps_daily[0] or 0))) + "°C"
        str_max = "{0:^7}".format(str_max)
        ver_text.insert(END, str_max, 'hot')
        ver_text.insert(END, "\n")

        today = datetime.today().weekday() + 1
        for i in range(1, len(self.days)):
            if today == 7:
                today = 0
            weekday = WEEKDAYS[today]

            str_now = "   " + "{0:^10}".format(weekday)
            ver_text.insert(END, str_now)

            str_min = str(round(int(self.min_temps_daily[i] or 0))) + "°C"
            str_min = "{0:^7}".format(str_min)
            ver_text.insert(END, str_min, 'cold')

            ver_text.image_create(END, image=photo1)

            str_max = str(round(int(self.max_temps_daily[i] or 0))) + "°C"
            str_max = "{0:^7}".format(str_max)
            ver_text.insert(END, str_max, 'hot')

            ver_text.insert(END, "\n")
            today += 1
            i += 1

        ver_text.config(state=DISABLED)
        ver_scroll.config(command=ver_text.yview)

        # Everything else frame:

        bottom_frame = Frame(frame)
        bottom_frame.pack(side=TOP)

        # wind:
        wind = "Wind speed:\n" + str(self.winds[self.index]) + " km/h"
        lbl_wind = Label(bottom_frame, text=wind, width=10, height=5, borderwidth=2, relief="groove")
        lbl_wind.pack(side=LEFT)

        # humidity:
        hum = "Humidity:\n" + str(self.hums[self.index]) + " %"
        lbl_hum = Label(bottom_frame, text=hum, width=10, height=5, borderwidth=2, relief="groove")
        lbl_hum.pack(side=LEFT, padx=2)

        # precipitation:
        prec = "Precipitation:\n" + str(self.precs[self.index]) + " %"
        lbl_prec = Label(bottom_frame, text=prec, width=10, height=5, borderwidth=2, relief="groove")
        lbl_prec.pack(side=LEFT)

        # Hourly + sun raise and set
        hourly = ""
        day = 0
        sunrise = self.sunrise_daily[day]
        sunrise = sunrise[len(sunrise) - 5:]
        sunset = self.sunset_daily[day]
        sunset = sunset[len(sunset) - 5:]
        for i in range(self.index + 1, len(self.times)):
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
