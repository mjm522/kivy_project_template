from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen


Builder.load_file('screen2/screen2.kv')


class Screen2(Screen):
    var1 = ObjectProperty()
    var1 = ObjectProperty()

    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)

    def button_b2a_handle(self):
        print("pressed b2a handle")

    def button_b2b_handle(self):
        print("pressed b2b handle")