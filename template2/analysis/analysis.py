from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

Builder.load_file('analysis/analysis.kv')


class Analysis(Screen):
    var1 = ObjectProperty()
    var1 = ObjectProperty()

    def __init__(self, **kwargs):
        super(Analysis, self).__init__(**kwargs)
        self.image_source = "images/analysis_button.jpg"

    def button_b1a_handle(self):
        print("pressed b1a handle")

    def button_b1b_handle(self):
        print("pressed b1b handle")