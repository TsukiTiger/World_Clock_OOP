import pytz
from datetime import datetime
from tkinter import *
import time


class Clock(Frame):
    def update_option(self, *args):
        cities = self.data[self.continentList.get()]
        self.cityList.set(cities[0])

        menu = self.cityMenu['menu']
        menu.delete(0, 'end')

        for city in cities:
            menu.add_command(label=city, command=lambda nation=city: self.cityList.set(nation))

    def __init__(self, window, continent, city, position, **kw):
        super().__init__(**kw)
        self.city = city
        self.continent = continent
        self.position = position
        self.window = window

        self.place = str(self.continent) + "/" + str(self.city)
        self.timezone = pytz.timezone(self.place)
        self.local_time = datetime.now(self.timezone)
        self.current_time = self.local_time.strftime("%H:%M:%S")

        self.cityLabel = Label(window, text=self.city, font=("times", 20, "bold"))
        self.cityLabel.place(x=30, y=(5 + (100 * self.position)))
        self.time = Label(window, text=self.current_time, font=("times", 33, "bold"))
        self.time.place(x=10, y=(40 + (100 * self.position)))
        self.nota = Label(window, text="Hours   Minutes   Seconds", font=("times", 10, "bold"))
        self.nota.place(x=10, y=(80 + (100 * self.position)))
        self.clockNumber = Label(window, text="Clock #"+str(position+1), font=("times", 12))
        self.clockNumber.place(x=170, y=(10+100*self.position))
        self.updateTime()

        self.buttonClicked = False

        if position >= 1:
            self.changeButton = Button(window, text="+", font=("times", 20, "bold"),
                                       command=lambda: self.newCity(self.continent, self.city))
            self.changeButton.place(x=200, y=(40 + (100 * position)))
            self.changeButton["state"] = "normal"
        else:
            self.LocalTimeLabel = Label(window,text="Local Time", font=("times", 13), fg="Red")
            self.LocalTimeLabel.place(x=163, y=40)

    def updateTime(self):
        self.place = str(self.continent) + "/" + str(self.city)
        self.timezone = pytz.timezone(self.place)
        self.local_time = datetime.now(self.timezone)
        self.current_time = self.local_time.strftime("%H:%M:%S")
        self.time.config(text=self.current_time)
        self.cityLabel.config(text=self.city)

    def newCity(self, continent, city):
        oldCity = city
        oldContinent = continent
        position = "+240+" + str(50+100*self.position)
        self.new_window = Toplevel(self.window)
        self.new_window.geometry("400x100"+position)
        new_window_name = "Choose a New City for Clock " + str(self.position + 1)
        self.new_window.title(new_window_name)
        self.changeButton["state"] = "disabled"
        self.data = {'Africa': ['Tunis', 'Accra', "Cairo", "Lusaka"],
                     'America': ['Chicago', 'Los_Angeles', 'Denver', 'Detroit', 'New_York', 'Mexico_City'],
                     'Asia': ['Bangkok', 'Chongqing', 'Dubai', 'Hong_Kong', 'Shanghai', 'Tokyo'],
                     'Australia': ['Brisbane', 'Canberra', 'Darwin', 'Melbourne', 'Sydney'],
                     'Europe': ['Berlin', 'Budapest', 'Copenhagen', 'Dublin', 'Lisbon', 'London', 'Moscow', 'Paris', 'Rome', 'Vienna'],
                     'Pacific': ['Auckland', 'Easter', 'Fiji', 'Honolulu', 'Midway', 'Palau', 'Saipan']}

        self.continentList = StringVar(self)
        self.cityList = StringVar(self)

        self.continentList.set(oldContinent)
        self.cityList.set(oldCity)

        self.continentMenu = OptionMenu(self.new_window, self.continentList, *self.data.keys())
        self.cityMenu = OptionMenu(self.new_window, self.cityList, '')
        self.attention = Label(self.new_window, text='Please click "Confirm" Button to exit.',
                               font=("times", 10, "bold"), fg="Red")

        self.continentList.trace('w', self.update_option)

        self.continentMenu.place(x=10, y=20)
        self.cityMenu.place(x=110, y=20)
        self.attention.place(x=100, y=1)

        self.confirmButton = Button(self.new_window, text="Confirm", font=("times", 20, "bold"),
                                    command=lambda: self.change(self.continentList.get(), self.cityList.get()))
        self.confirmButton.place(x=250, y=20)
        self.updateTime()

    def change(self, new_continent, new_city):
        self.continent = new_continent
        self.city = new_city
        self.changeButton["state"] = "normal"
        self.new_window.destroy()
