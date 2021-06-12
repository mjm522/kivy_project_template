from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelStrip
from kivy.lang import Builder


class MovableTabs(TabbedPanel):

    def __init__(self, **kwargs):
        super(MovableTabs, self).__init__(**kwargs)
        self.initialTabHeight = None
        self.myTabsList = None
        self.start_top = None
        self.tabs_showing = True

        # this TabbedPanelStrip will be a copy of the real one (self._tab_strip)
        self.tmp_tab_strip = TabbedPanelStrip(
            tabbed_panel=self,
            rows=1, size_hint=(None, None),
            height=self.tab_height, width=self.tab_width)

        # this is the movable Widget that contains the tabs
        self.movable_tab_strip = ScrollView(size_hint=(None, None), height=self.tab_height)

        # These value are needed to set the width of self.movable_tab_strip, but
        # they aren't always available when self.first is called below
        self._tab_strip.bind(width=self.tab_strip_width_changed)
        self.bind(width=self.panel_width_changed)

        # Clock.schedule_once(self.first)

    def tab_strip_width_changed(self, instance, new_width):
        self.movable_tab_strip.width = min(self.tmp_tab_strip.width, self.width)

    def panel_width_changed(self, instance, new_width):
        self.movable_tab_strip.width = min(self.tmp_tab_strip.width, self.width)

    def first(self, *args):
        # show tab2, so that the Button will be available
        self.switch_to(self.parent.ids.tab2)

        # save some info
        self.initialTabHeight = self.tab_height
        self.myTabsList = self.tab_list.copy()

        tsw = 0
        for tab in self.myTabsList:
            if tab.size_hint_x:
                tsw += 100
            else:
                tsw += tab.width
        self.tmp_tab_strip.width = tsw
        self.movable_tab_strip.add_widget(self.tmp_tab_strip)

        # actually remove the tabs
        self.do_clear_widgets()

    def do_clear_widgets(self, *args):
        # eliminate the tabs and populate the moveable_tab_strip
        #self.movable_tab_strip.width = min(self.tmp_tab_strip.width, self.width)
        self.tab_height = 0
        self.clear_tabs()
        for tab in reversed(self.myTabsList):
            self.tmp_tab_strip.add_widget(tab)
        self.tabs_showing = False

    def do_progress(self, animation, widget, progression):
        # grow the tab height when the moveable_tab_strip impinges on the TabbedPanel
        # this has the effect of appearing to shrink the TappedPanel to the size it will have when the tabs are replaced
        if self.start_top > self.movable_tab_strip.y:
            self.tab_height = self.start_top - self.movable_tab_strip.y

    def do_replace_tabs(self, *args):
        # replace the moveable_tab_trip with the actual tabs
        self.tmp_tab_strip.clear_widgets()
        for tab in reversed(self.myTabsList):
            self.add_widget(tab)
        self.tab_height = self.initialTabHeight
        self.parent.remove_widget(self.movable_tab_strip)

    def do_tab_toggle(self, *args):
        if self.tabs_showing:
            self.do_clear_widgets()
        else:
            self.anim = Animation(pos=(self.x+2, self.y + self.height - self.movable_tab_strip.height))
            self.movable_tab_strip.pos = (self.x + 2, App.get_running_app().root_window.height)
            self.start_top = self.top
            self.parent.add_widget(self.movable_tab_strip)
            # self.anim.bind(on_progress=self.do_progress)
            self.anim.bind(on_complete=self.do_replace_tabs)
            self.anim.start(self.movable_tab_strip)
            self.tabs_showing = True
