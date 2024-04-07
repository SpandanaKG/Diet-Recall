from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivy.core.window import Window
from kivy.lang import Builder

Window.size = (397, 697)

KV = '''
BoxLayout:
    orientation: 'vertical'
    MDTopAppBar:
        title: 'Snacks'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y":.05}
            on_release: app.root.current = 'menu'

    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch(*args)

<FirstTab>
    name: 'first_tab'
    title:'My Snack'
    ScreenManager:
        Screen:
            name:"Screen"
            Snack:
                orientation: 'vertical'
                

                MDTextField:
                    hint_text: "Enter the item"
                    pos_hint:{'center_x': 0.5, 'center_y': 0.65}
                    size_hint_x:0.6
                    height: dp(30)
                MDRectangleFlatButton:
                    text: 'Submit'
                    size_hint_y: None
                    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
                    height: dp(40)
                    on_release:
                        app.root.current='menu' 
<SecondTab>
    name: 'second_tab'
    title:'Suggestion'
    MDLabel:
        text: 'Database should be created'
        halign: 'center'


'''




class Snack(Screen):
    pass





class FirstTab(MDScreen, MDTabsBase):
    pass


class SecondTab(MDScreen, MDTabsBase):
    pass


class TestApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

    def on_start(self):
        # Add tabs dynamically
        self.root.ids.tabs.add_widget(FirstTab())
        self.root.ids.tabs.add_widget(SecondTab())

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        pass


TestApp().run()