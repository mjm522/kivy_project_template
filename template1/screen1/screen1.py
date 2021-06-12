from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen


Builder.load_file('screen1/screen1.kv')


class Screen1(Screen):
    var1 = ObjectProperty()
    var1 = ObjectProperty()

    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)

    def button_b1a_handle(self):
        print("pressed b1a handle")

    def button_b1b_handle(self):
        print("pressed b1b handle")