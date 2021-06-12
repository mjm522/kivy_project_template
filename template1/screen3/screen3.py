from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen


Builder.load_file('screen3/screen3.kv')


class Screen3(Screen):
    var1 = ObjectProperty()
    var1 = ObjectProperty()

    def __init__(self, **kwargs):
        super(Screen3, self).__init__(**kwargs)

    def button_b3a_handle(self):
        print("pressed b3a handle")

    def button_b3b_handle(self):
        print("pressed b3b handle")