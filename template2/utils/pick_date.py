from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivymd.uix.picker import MDDatePicker
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

# KV = '''
# <DatePicker>:
#     text_id: date_text
#     GridLayout:
#         cols:1
#         Label:
#             id: date_text
#             text: 'Date: '
#         Button:
#             text: "Open time picker"
#             pos_hint: {'center_x': .5, 'center_y': .5}
#             on_release: app.show_date_picker()
# '''

# Builder.load_file('payments/payment_tabs.kv')


class DatePicker(FloatLayout):
    text_id = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(DatePicker, self).__init__(**kwargs)

    def on_save(self, instance):
        self.text_id.text = instance

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.on_save)
        date_dialog.open()


# class MultitabScreen(Screen):
#     var1 = ObjectProperty()
#     var1 = ObjectProperty()

#     def __init__(self, **kwargs):
#         super(MultitabScreen, self).__init__(**kwargs)
#         self.add_widget(PaymentTabs())

# class DatePicker(Screen):
#     def __init__(self, **kwargs):



# class DatePicker(MDApp):
    
#     text_id = ObjectProperty(None)
    
#     def build(self):
#         return Builder.load_string(KV)

#     def on_save(self, instance):
#         self.text_id.text = instance

#     def show_date_picker(self):
#         date_dialog = MDDatePicker(callback=self.on_save)
#         date_dialog.open()





# DatePicker().run()