from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.tabbedpanel import TabbedPanelItem

Builder.load_file('settings/settings.kv')


class Settings(Screen):
    var1 = ObjectProperty()
    var1 = ObjectProperty()

    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)

    def button_b11a_handle(self):
        print("pressed b11a handle")

    def button_b11b_handle(self):
        print("pressed b11b handle")