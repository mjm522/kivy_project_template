from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.picker import MDDatePicker


Builder.load_file('payments/payment_tabs.kv')


class PaymentTabs(FloatLayout):
    pass


class MultitabScreen(Screen):
    date = None
    var1 = ObjectProperty()

    def __init__(self, **kwargs):
        super(MultitabScreen, self).__init__(**kwargs)
        self.add_widget(PaymentTabs())

