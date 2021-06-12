from kivy.lang import Builder
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.tabbedpanel import TabbedPanel 
from kivy.config import Config
from kivymd.uix.picker import MDDatePicker
from kivy.properties import ObjectProperty


Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '700')
Config.write()


class TabManager(TabbedPanel):

    def __init__(self, **kwargs):
        super(TabManager, self).__init__(**kwargs)
        self._date = None

    def on_save(self, instance):
        print(instance)
        print(type(instance))
        print(self.ids.multitab_screen_payments.date )
        print(self.ids.multitab_screen_payments.ids )
        self._date = instance
        # self.ids.multitab_screen_payments.date = instance

    def open_date_picker(self):
        date_dialog = MDDatePicker(callback=self.on_save)
        date_dialog.open()


class LedgerApp(MDApp):
    def build(self):
        return Builder.load_file('main.kv')

    


if __name__ == "__main__":
    LedgerApp().run()
