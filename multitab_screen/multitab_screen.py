from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.tabbedpanel import TabbedPanel


Builder.load_file('multitab_screen/multitab_screen.kv')


class MultitabTest(TabbedPanel):
    pass


class MultitabScreen(Screen):
    var1 = ObjectProperty()
    var1 = ObjectProperty()

    def __init__(self, **kwargs):
        super(MultitabScreen, self).__init__(**kwargs)
        self.add_widget(MultitabTest())
        