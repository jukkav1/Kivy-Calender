# Project made by: Kuldeep Singh
# Student at LNMIIT,Jaipur,India;

# Typos, python3 etc fixes and further dev by:
# Jukka Valvanne

# import statements
import calendar
import time
import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Builder used to load all the kivy files to be loaded in the main.py file
Builder.load_file("months.kv")
Builder.load_file("dates.kv")
Builder.load_file("select.kv")
Builder.load_file("status.kv")
Builder.load_file("days.kv")


# class for calender.kv file
class Calendar(BoxLayout):
    def __init__(self, **kwargs):
        super(Calendar, self).__init__(**kwargs)


# ------------------------------------------------------------------------------------------------#


# class for status.kv file
class Status(BoxLayout):
    def __init__(self, **kwargs):
        super(Status, self).__init__(**kwargs)


# ------------------------------------------------------------------------------------------------#


# class for select.kv file
class Select(BoxLayout):
    number = ListProperty()
    year = ObjectProperty(None)
    lbl = ObjectProperty(None)
    btn = ObjectProperty(None)
    global count

    def __init__(self, **kwargs):
        super(Select, self).__init__(**kwargs)
        self.count = 0

    def get_years(self):
        """Tää on outo härveli."""
        if self.count == 0:
            for _ in range(2000, 2050):
                self.number.append(str(_))
        self.count = 1
        self.year.values = self.number


# ------------------------------------------------------------------------------------------------#


# class for Reminder in Dates
class Reminder(BoxLayout):
    def __init__(self, **kwargs):
        super(Reminder, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.textbox = TextInput()
        self.b = BoxLayout(orientation="horizontal", size_hint=(1, 0.15))
        self.add_widget(self.textbox)
        self.add_widget(self.b)
        self.b.add_widget(Button(on_release=self.on_release, text="Tallenna"))
        pass

    def on_release(self, e):
        print("Yritetty tallentaa", self.textbox.text)


# ------------------------------------------------------------------------------------------------#


# class for dates.kv file
class Dates(GridLayout):
    now = datetime.datetime.now()

    def __init__(self, **kwargs):
        super(Dates, self).__init__(**kwargs)
        self.cols = 7

        # Kalenteri näyttää lähtökohtaisesti kuluvan kuun kalenteria
        self.c = calendar.monthcalendar(self.now.year, self.now.month)

        for i in self.c:
            for j in i:
                if j == 0:
                    self.add_widget(
                        Button(on_release=self.on_release, text="{j}".format(j=""))
                    )
                else:
                    self.add_widget(
                        Button(on_release=self.on_release, text="{j}".format(j=j))
                    )

    def get_month(self):
        pass

    def on_dismiss(self, arg):
        print("Dismissed :()")
        # Do something on close of popup
        pass

    def on_release(self, event):
        print("Valittu päivä: " + event.text)
        event.background_color = 1, 0, 0, 1
        self.popup = Popup(
            title="Tee merkintä",
            content=Reminder(),
            size_hint=(None, None),
            size=(self.width * 3 / 4, self.height),
        )
        self.popup.bind(on_dismiss=self.on_dismiss)
        self.popup.open()


# ------------------------------------------------------------------------------------------------#


# class for months.kv file
class Months(BoxLayout):
    def __init__(self, **kwargs):
        super(Months, self).__init__(**kwargs)


# ------------------------------------------------------------------------------------------------#


# mainApp class
class mainApp(App):
    time = StringProperty()

    def update(self, *args):
        self.time = str(time.asctime())

    def build(self):
        self.title = "Kivy-Calendar"
        self.load_kv("calendar.kv")
        Clock.schedule_interval(self.update, 1)
        return Calendar()


# BoilerPlate
if __name__ == "__main__":
    app = mainApp()
    app.run()
