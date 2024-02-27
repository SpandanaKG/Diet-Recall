from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.navigationdrawer import MDNavigationLayout,MDNavigationDrawer
from kivymd.uix.toolbar import MDTopAppBar

Window.size = (397, 697)



KV= '''
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
                    Widget: 
                    BoxLayoutExample:
                        orientation:'vertical'
        MDNavigationDrawer:
            id: nav_drawer
'''

class BoxLayoutExample(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        eat = MDRectangleFlatButton(text="Eaten\n\n____kcal", pos_hint={'center_x': 0.21, 'y': .7})
        eat1 = MDRectangleFlatButton(text="Calories\n\n Remaining\n\n____kcal", pos_hint={'center_x': 0.51, 'y': .7})
        eat2 = MDRectangleFlatButton(text="Water\n\nTanker", pos_hint={'center_x': 0.79, 'y': .7})
        btn_flat = MDRectangleFlatButton(text="BreakFast\n___Recommended cal\n___cal consumed ", halign="left",
                                         pos_hint={'center_x': 0.5, 'y': 0.5}, size_hint=(.78, 0))
        btn_icon = MDFloatingActionButton(icon="plus", halign="right", pos_hint={'center_x': .81, 'y': 0.51})
        btn_flat1 = MDRectangleFlatButton(text="Lunch\n___Recommended cal\n___cal consumed ", halign="left",
                                          pos_hint={'center_x': 0.5, 'y': 0.375},
                                          size_hint=(.78, 0))
        btn_icon2 = MDFloatingActionButton(icon="plus", halign="right", pos_hint={'center_x': .81, 'y': 0.385})
        btn_flat2 = MDRectangleFlatButton(text="Snacks\n___Recommended cal\n___cal consumed ", halign="left",
                                          pos_hint={'center_x': 0.5, 'y': 0.25},
                                          size_hint=(.78, 0))
        btn_icon3 = MDFloatingActionButton(icon="plus", halign="right", pos_hint={'center_x': .81, 'y': 0.26})
        btn_flat3 = MDRectangleFlatButton(text="Dinner\n___Recommended cal\n___cal consumed ", halign="left",
                                          pos_hint={'center_x': 0.5, 'y': 0.125},
                                          size_hint=(.78, 0))
        btn_icon4 = MDFloatingActionButton(icon="plus", halign="right", pos_hint={'center_x': .81, 'y': 0.135})
        btn1 = MDFlatButton(text="Home", pos_hint={'center_x': .2, 'center_y': 0.065}, md_bg_color="#009cff")
        btn2 = MDFlatButton(text="Favorites", pos_hint={'center_x': .5, 'center_y': 0.065}, md_bg_color="#009cff")
        btn3 = MDFlatButton(text="Meal Planner", pos_hint={'center_x': .8, 'center_y': 0.065}, md_bg_color="#009cff")
        self.add_widget(eat)
        self.add_widget(eat1)
        self.add_widget(eat2)
        self.add_widget(btn_flat)
        self.add_widget(btn_flat1)
        self.add_widget(btn_flat2)
        self.add_widget(btn_flat3)
        self.add_widget(btn_icon)
        self.add_widget(btn_icon2)
        self.add_widget(btn_icon3)
        self.add_widget(btn_icon4)
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
class DietRecallApp(MDApp):
    def build(self):
        screen=Builder.load_string(KV)
        theme_cls=ThemeManager()
        self.theme_cls.primary_palette = ("Blue")
        self.theme_cls.primary_hue="A700"
        self.theme_cls.theme_style=("Light")



        return screen

DietRecallApp().run()
