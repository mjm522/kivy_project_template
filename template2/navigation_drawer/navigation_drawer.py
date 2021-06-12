from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

Builder.load_file('navigation_drawer/navigation_drawer.kv')


class ContentNavigationDrawer(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

    def __init__(self, **kwargs):
        super(ContentNavigationDrawer, self).__init__(**kwargs)