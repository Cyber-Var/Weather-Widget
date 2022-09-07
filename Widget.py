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

PHOTOS = {
    0: ImageTk.PhotoImage(Image.open("resources/0_d.jpg").resize((70, 70), Image.ANTIALIAS)),
    1: ImageTk.PhotoImage(Image.open("resources/1_d.jpg").resize((70, 70), Image.ANTIALIAS)),
    2: ImageTk.PhotoImage(Image.open("resources/1_d.jpg").resize((70, 70), Image.ANTIALIAS)),
    3: ImageTk.PhotoImage(Image.open("resources/1_d.jpg").resize((70, 70), Image.ANTIALIAS)),
    4: ImageTk.PhotoImage(Image.open("resources/0_n.jpg").resize((70, 70), Image.ANTIALIAS)),
    5: ImageTk.PhotoImage(Image.open("resources/1_n.jpg").resize((70, 70), Image.ANTIALIAS)),
    45: ImageTk.PhotoImage(Image.open("resources/45.jpg").resize((70, 70), Image.ANTIALIAS)),
    48: ImageTk.PhotoImage(Image.open("resources/45.jpg").resize((70, 70), Image.ANTIALIAS)),
    51: ImageTk.PhotoImage(Image.open("resources/51.jpg").resize((70, 70), Image.ANTIALIAS)),
    53: ImageTk.PhotoImage(Image.open("resources/51.jpg").resize((70, 70), Image.ANTIALIAS)),
    55: ImageTk.PhotoImage(Image.open("resources/55.jpg").resize((70, 70), Image.ANTIALIAS)),
    56: ImageTk.PhotoImage(Image.open("resources/51.jpg").resize((70, 70), Image.ANTIALIAS)),
    57: ImageTk.PhotoImage(Image.open("resources/55.jpg").resize((70, 70), Image.ANTIALIAS)),
    61: ImageTk.PhotoImage(Image.open("resources/55.jpg").resize((70, 70), Image.ANTIALIAS)),
    63: ImageTk.PhotoImage(Image.open("resources/63.jpg").resize((70, 70), Image.ANTIALIAS)),
    65: ImageTk.PhotoImage(Image.open("resources/63.jpg").resize((70, 70), Image.ANTIALIAS)),
    66: ImageTk.PhotoImage(Image.open("resources/55.jpg").resize((70, 70), Image.ANTIALIAS)),
    67: ImageTk.PhotoImage(Image.open("resources/63.jpg").resize((70, 70), Image.ANTIALIAS)),
    71: ImageTk.PhotoImage(Image.open("resources/71.jpg").resize((70, 70), Image.ANTIALIAS)),
    73: ImageTk.PhotoImage(Image.open("resources/73.jpg").resize((70, 70), Image.ANTIALIAS)),
    75: ImageTk.PhotoImage(Image.open("resources/75.jpg").resize((70, 70), Image.ANTIALIAS)),
    77: ImageTk.PhotoImage(Image.open("resources/77.jpg").resize((70, 70), Image.ANTIALIAS)),
    80: ImageTk.PhotoImage(Image.open("resources/80.jpg").resize((70, 70), Image.ANTIALIAS)),
    81: ImageTk.PhotoImage(Image.open("resources/81.jpg").resize((70, 70), Image.ANTIALIAS)),
    82: ImageTk.PhotoImage(Image.open("resources/82.jpg").resize((70, 70), Image.ANTIALIAS)),
    85: ImageTk.PhotoImage(Image.open("resources/85.jpg").resize((70, 70), Image.ANTIALIAS)),
    86: ImageTk.PhotoImage(Image.open("resources/85.jpg").resize((70, 70), Image.ANTIALIAS)),
    95: ImageTk.PhotoImage(Image.open("resources/95.jpg").resize((70, 70), Image.ANTIALIAS)),
    96: ImageTk.PhotoImage(Image.open("resources/95.jpg").resize((70, 70), Image.ANTIALIAS)),
    99: ImageTk.PhotoImage(Image.open("resources/95.jpg").resize((70, 70), Image.ANTIALIAS)),
    100: ImageTk.PhotoImage(Image.open("resources/sunrise.jpg").resize((70, 70), Image.ANTIALIAS)),
    200: ImageTk.PhotoImage(Image.open("resources/sunset.jpg").resize((70, 70), Image.ANTIALIAS)),
    300: ImageTk.PhotoImage(Image.open("resources/wind.jpg").resize((30, 30), Image.ANTIALIAS)),
    400: ImageTk.PhotoImage(Image.open("resources/hum.jpg").resize((30, 30), Image.ANTIALIAS)),
    500: ImageTk.PhotoImage(Image.open("resources/prec.jpg").resize((30, 30), Image.ANTIALIAS)),
}

'''PHOTOS = {
    0: ImageTk.PhotoImage(Image.open("resources/0_d.jpg").resize((70, 70), Image.ANTIALIAS)),
    1: "1", 2: "1", 3: "1",
    45: "45", 48: "45",
    51: "51", 53: "51", 55: "55",
    56: "51", 57: "55",
    61: "55", 63: "63", 65: "63",
    66: "55", 67: "63",
    71: "71", 73: "73", 75: "75",
    77: "77",
    80: "80", 81: "81", 82: "82",
    85: "85", 86: "85",
    95: "95",
    96: "95", 99: "95"
}'''

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

        # Main Frame:

        top_frame = Frame(frame, width=width, height=200)
        top_frame.pack(side=TOP)

        wmo = self.wmos[self.index]
        temp = str(self.temps[self.index]) + " °C"
        max_min = "max.: " + str(self.max_temps_daily[0]) + " °C" + ", min.: " + str(self.min_temps_daily[0]) + " °C"

        lbl_icon = Label(top_frame, image=PHOTOS[self.wmos[self.index]])
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
        su_t_int = int(sunset_today[len(sunset_today) - 5:len(sunset_today) - 3])
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

        for i in range(self.index, self.index + 24):
            t = str(self.times[i])
            t = int(t[len(t) - 5:len(t) - 3])
            ti = str(t) + ":00 "
            if i == self.index:
                ti = "Now"
            str_time = "{0:^10}".format(ti)
            hor_text.insert(END, str_time)
            if sunrise == t:
                str_time = "{0:^10}".format(sunrise_time)
                hor_text.insert(END, str_time)
            elif sunset == t:
                str_time = "{0:^10}".format(sunset_time)
                hor_text.insert(END, str_time)
        hor_text.insert(END, "\n")

        for i in range(self.index, self.index + 24):
            t = str(self.times[i])
            t = int(t[len(t) - 5:len(t) - 3])
            hor_text.image_create(END, image=PHOTOS[round(self.wmos[i])])
            if sunrise == t:
                hor_text.image_create(END, image=PHOTOS[100])
            elif sunset == t:
                hor_text.image_create(END, image=PHOTOS[200])
        hor_text.insert(END, "\n")

        for i in range(self.index, self.index + 24):
            t = str(self.times[i])
            t = int(t[len(t) - 5:len(t) - 3])
            te = round(int(self.temps[i] or 0))
            te = str(te) + "°C"
            str_temp = "{0:^10}".format(te)
            hor_text.insert(END, str_temp)
            if sunrise == t:
                str_temp = "{0:^10}".format("Sunrise")
                hor_text.insert(END, str_temp)
            if sunset == t:
                str_temp = "{0:^10}".format("Sunset")
                hor_text.insert(END, str_temp)

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

        lbl_wind = Label(bottom_frame, text="Wind speed:")
        lbl_wind.grid(row=0, column=0)
        lbl_wind1 = Label(bottom_frame, image=PHOTOS[300])
        lbl_wind1.grid(row=1, column=0)
        lbl_wind2 = Label(bottom_frame, text=str(self.winds[self.index]) + " km/h")
        lbl_wind2.grid(row=2, column=0)

        lbl_hum = Label(bottom_frame, text="Humidity:")
        lbl_hum.grid(row=0, column=1)
        lbl_hum1 = Label(bottom_frame, image=PHOTOS[400])
        lbl_hum1.grid(row=1, column=1)
        lbl_hum2 = Label(bottom_frame, text=str(round(self.hums[self.index])) + " %")
        lbl_hum2.grid(row=2, column=1)

        lbl_prec = Label(bottom_frame, text="Precipitation:")
        lbl_prec.grid(row=0, column=2)
        lbl_prec1 = Label(bottom_frame, image=PHOTOS[500])
        lbl_prec1.grid(row=1, column=2)
        lbl_prec2 = Label(bottom_frame, text=str(self.precs[self.index]) + " %")
        lbl_prec2.grid(row=2, column=2)

        ''''# wind:
        canvas_wind = Canvas(frame, width=50, height=50)
        canvas_wind.pack(side=LEFT)

        canvas_wind.create_text("Wind speed:")
        canvas_wind.create_image(30, 30, anchor=NW, image=PHOTOS[300])
        canvas_wind.create_text(str(self.winds[self.index]) + " km/h")'''

        '''wind = "Wind speed:\n" + str(self.winds[self.index]) + " km/h"
        lbl_wind = Label(bottom_frame, text=wind, width=10, height=5, borderwidth=2, relief="groove")
        lbl_wind.pack(side=LEFT)'''

        ''''# humidity:
        hum = "Humidity:\n" + str(self.hums[self.index]) + " %"
        lbl_hum = Label(bottom_frame, text=hum, width=10, height=5, borderwidth=2, relief="groove")
        lbl_hum.pack(side=LEFT, padx=2)

        # precipitation:
        prec = "Precipitation:\n" + str(self.precs[self.index]) + " %"
        lbl_prec = Label(bottom_frame, text=prec, width=10, height=5, borderwidth=2, relief="groove")
        lbl_prec.pack(side=LEFT)'''

        root.mainloop()

    def print_data(self):
        print(self.data)
