import sqlite3

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from login import LoginUI

Window.size = (370, 697)

email=""

KV = """

ScreenManager:
    MenuScreen:
    ProfileScreen:
    ChallengesScreen:
    FeedbackScreen:
    SettingsScreen:
    LogoutScreen:
    LoginScreen:

<MenuScreen>:
    name:'menu'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                id:screen_manager
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title:'Home'
                            elevation: 10
                            left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
                            pos_hint:{"top": 1}
                        Widget: 
                        MDScreen:
                            Menu:
                                height:'75dp'                
            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    padding: '8dp'
                    spacing: '20dp'

                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Home'
                                IconLeftWidget:
                                    icon: 'home' 
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='menu'
                            OneLineIconListItem:
                                text: 'Profile'
                                IconLeftWidget:
                                    icon: 'face-woman-profile'
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='profile'
                            OneLineIconListItem:
                                text: 'Challenges'
                                IconLeftWidget:
                                    icon: 'fire'
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='challenges'                                    
                            OneLineIconListItem:
                                text: 'Feedback'
                                IconLeftWidget:
                                    icon: 'graph-outline'  
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='feedback'                                                              
                            OneLineIconListItem:
                                text: 'Settings'
                                IconLeftWidget:
                                    icon: 'screwdriver'
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='settings'                                    
                            OneLineIconListItem:
                                text: 'Logout'  
                                IconLeftWidget:
                                    icon: 'logout-variant'  
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='logout'                                    

<ProfileScreen>:
    name:'profile'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                id:screen_manager
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title:'Profile'
                            elevation: 10
                            left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
                            pos_hint:{"top": 1}
                        Widget:
                        MDScreen:  
                            Profile:
                                id:'prof'
                                height: '75dp'

            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    padding: '8dp'
                    spacing: '20dp'

                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Home'
                                IconLeftWidget:
                                    icon: 'home' 
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='menu'
                            OneLineIconListItem:
                                text: 'Profile'
                                IconLeftWidget:
                                    icon: 'face-woman-profile'
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='profile'
                            OneLineIconListItem:
                                text: 'Challenges'
                                IconLeftWidget:
                                    icon: 'fire'
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='challenges'
                            OneLineIconListItem:
                                text: 'Feedback'
                                IconLeftWidget:
                                    icon: 'graph-outline'  
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='feedback'                          
                            OneLineIconListItem:
                                text: 'Settings'
                                IconLeftWidget:
                                    icon: 'screwdriver'
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='settings'
                            OneLineIconListItem:
                                text: 'Logout'  
                                IconLeftWidget:
                                    icon: 'logout-variant'  
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='logout'    

<ChallengesScreen>:
    name:'challenges'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                id:screen_manager
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title:'Challenges'
                            elevation: 10
                            left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
                            pos_hint:{"top": 1}
                        Widget:
                        MDScreen:
                            MDLabel:
                                text:"Database to be designed"
                                halign: 'center'
                                pos_hint: {'center_x': .52, 'y': .7}

            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    padding: '8dp'
                    spacing: '20dp'

                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Home'
                                IconLeftWidget:
                                    icon: 'home' 
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='menu'
                            OneLineIconListItem:
                                text: 'Profile'
                                IconLeftWidget:
                                    icon: 'face-woman-profile'
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='profile'
                            OneLineIconListItem:
                                text: 'Challenges'
                                IconLeftWidget:
                                    icon: 'fire'
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='challenges'
                            OneLineIconListItem:
                                text: 'Feedback'
                                IconLeftWidget:
                                    icon: 'graph-outline'  
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='feedback'                          
                            OneLineIconListItem:
                                text: 'Settings'
                                IconLeftWidget:
                                    icon: 'screwdriver'
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='settings'
                            OneLineIconListItem:
                                text: 'Logout'  
                                IconLeftWidget:
                                    icon: 'logout-variant'  
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='logout'

<FeedbackScreen>:
    name:'feedback'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                id:screen_manager1
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title:'FeedBack'
                            elevation: 10
                            left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
                            pos_hint:{"top": 1}
                        Widget:
                        MDScreen:
                            id:"class_f"
                            Feed:
                                id : 'fed'
                                height: '75dp'
            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    padding: '8dp'
                    spacing: '20dp'

                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Home'
                                IconLeftWidget:
                                    icon: 'home' 
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='menu'
                            OneLineIconListItem:
                                text: 'Profile'
                                IconLeftWidget:
                                    icon: 'face-woman-profile'
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='profile'
                            OneLineIconListItem:
                                text: 'Challenges'
                                IconLeftWidget:
                                    icon: 'fire'
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='challenges'
                            OneLineIconListItem:
                                text: 'Feedback'
                                IconLeftWidget:
                                    icon: 'graph-outline'  
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='feedback'                          
                            OneLineIconListItem:
                                text: 'Settings'
                                IconLeftWidget:
                                    icon: 'screwdriver'
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='settings'
                            OneLineIconListItem:
                                text: 'Logout'  
                                IconLeftWidget:
                                    icon: 'logout-variant'  
                                    on_release: 
                                        nav_drawer.set_state('close')
                                        app.root.current='logout'
<SettingsScreen>:
    name:'settings'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                id:screen_manager
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            pos_hint: {"top": 1}
                            elevation: 10
                            size_hint_y: None
                            height: dp(56)
                            padding: dp(10), dp(10)  
                            MDIconButton:
                                icon: "arrow-left"
                                pos_hint: {"center_y": .97}
                                on_release: app.root.current = 'menu'
                        Widget:
                        MDScreen:
                            height: '75dp'
                            FloatLayout:
                                height: '75dp'
                            MDLabel:
                                text: 'Dark Theme:'
                                pos_hint: {'center_x': .6, 'y': 1.291}
                                font_size: '22sp'
                            MDSwitch:
                                pos_hint: {'center_x': .8, 'y': 1.7}
                                on_active: app.on_switch_active(*args)

<LogoutScreen>:
    name:'logout'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                id:screen_manager
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            pos_hint: {"top": 1}
                            elevation: 10
                            size_hint_y: None
                            height: dp(56)
                            padding: dp(10), dp(10)  
                            MDIconButton:
                                icon: "arrow-left"
                                pos_hint: {"center_y": .97}
                                on_release: app.root.current = 'menu'
                        Widget:
                        MDScreen:
                            Log:
                                height:'75dp'


<LoginScreen>:
    name:'login'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                id:screen_manager
                MDScreen:
                    MDLabel:
                        text:'HelloWorld'
                        halign: 'center'

"""

username_helper = """
MDScreen:
    id:'pro'
    height: '75dp'
    text:"The end"
    MDTextField:
        hint_text:'name'
        size_hint_x:None
        width:300
        pos_hint:{'center_x':.5,'y':1.2}
        multiline:False
    MDTextField:
        hint_text:'Age'
        size_hint_x:None
        width:300
        pos_hint:{'center_x':.5,'y':1}
        multiline:False
    MDTextField:
        hint_text:'Sex'
        size_hint_x:None
        width:300
        pos_hint:{'center_x':.5,'y':.8}
        multiline:False
    MDTextField:
        hint_text:'Activity'
        size_hint_x:None
        width:300
        pos_hint:{'center_x':.5,'y':.6}
        multiline:False    
    MDTextField:
        hint_text:'Weight'
        size_hint_x:None
        width:300
        pos_hint:{'center_x':.5,'y':.4}  
        multiline:False  
    MDRectangleFlatButton:
        text:"Submit"
        pos_hint:{'center_x':.5,'center_y':.3}
        on_release:
            app.show_popup1()
"""

feedback_helper = """
MDScreen:
    id: fed1
    height: '75dp'
    MDTextField:
        id: text_input
        hint_text: 'FEEDBACK'
        size_hint_x: None
        width: 300
        pos_hint: {'center_x': .5, 'y': 1.2}
        multiline: True
    MDRectangleFlatButton:
        text: "Submit"
        pos_hint: {'center_x': .5, 'center_y': .9}
        on_release:
            app.show_popup()
"""


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class ChallengesScreen(Screen):
    pass


class FeedbackScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class LogoutScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class Menu(Screen):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        eat = MDRectangleFlatButton(text="Eaten\n\n____kcal", size_hint=(.15, .31),
                                    pos_hint={'center_x': 0.21, 'y': 1.55})
        eat1 = MDRectangleFlatButton(text="Calories\n\n Remaining\n\n____kcal", size_hint=(.15, .31),
                                     pos_hint={'center_x': 0.79, 'y': 1.55})
        btn_flat = MDRectangleFlatButton(text="BreakFast\n___Recommended cal\n___cal consumed ", halign="left",
                                         pos_hint={'center_x': 0.5, 'y': 1.25}, size_hint=(.78, 0),
                                         on_release=self.on_button_press)
        btn_icon = MDIconButton(icon="plus", halign="right", pos_hint={'center_x': .81, 'y': 1.27})
        btn_flat1 = MDRectangleFlatButton(text="Lunch\n___Recommended cal\n___cal consumed ", halign="left",
                                          pos_hint={'center_x': 0.5, 'y': 1}, size_hint=(.78, 0))
        btn_icon2 = MDIconButton(icon="plus", halign="right", pos_hint={'center_x': .81, 'y': 1.02})
        btn_flat2 = MDRectangleFlatButton(text="Snacks\n___Recommended cal\n___cal consumed ", halign="left",
                                          pos_hint={'center_x': 0.5, 'y': .75}, size_hint=(.78, 0))
        btn_icon3 = MDIconButton(icon="plus", halign="right", pos_hint={'center_x': .81, 'y': 0.77})
        btn_flat3 = MDRectangleFlatButton(text="Dinner\n___Recommended cal\n___cal consumed ", halign="left",
                                          pos_hint={'center_x': 0.5, 'y': 0.5}, size_hint=(.78, 0))
        btn_icon4 = MDIconButton(icon="plus", halign="right", pos_hint={'center_x': .81, 'y': 0.52})
        btn1 = MDFlatButton(text="Favorites", pos_hint={'center_x': .2, 'center_y': 0.30}, md_bg_color="#00e77a",
                            on_release=self.on_button_press)
        btn2 = MDFlatButton(text="Water Tanker", pos_hint={'center_x': .5, 'center_y': 0.30}, md_bg_color="#00e77a",
                            on_release=self.on_button_press1)
        btn3 = MDFlatButton(text="Meal Planner", pos_hint={'center_x': .8, 'center_y': 0.30}, md_bg_color="#00e77a",
                            on_release=self.on_button_press2)
        self.add_widget(eat)
        self.add_widget(eat1)
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

    def on_button_press(self, instance):
        # app = MDApp.get_running_app()
        # app.root.current = brekie()
        print("BTS!!!!")

    def on_button_press1(self, instance):
        # app = MDApp.get_running_app()
        # app.root.current = 'menu'
        print("The Love")

    def on_button_press2(self, instance):
        # app = MDApp.get_running_app()
        # app.root.current = 'menu'
        print("The Favourites!!")


class Profile(Screen):
    def __init__(self, **kwargs):
        super(Profile, self).__init__(**kwargs)
        img = Image(source='profile1.jpg', size_hint=(.15, .31), pos_hint={'center_x': 0.51, 'y': 1.55})
        self.username = Builder.load_string(username_helper)
        self.add_widget(self.username)
        self.add_widget(img)
        email = LoginUI.proceed(self)


global user_feed
global feed_obj
class Feed(Screen):
    def __init__(self, **kwargs):
        super(Feed, self).__init__(**kwargs)
        self.feedback = Builder.load_string(feedback_helper)
        self.add_widget(self.feedback)
          # Define user_feed as global
        self.screen_text = self.feedback.ids.text_input
        user_feed = self.screen_text
        feed_obj = self

class Log(Screen):
    def __init__(self, **kwargs):
        super(Log, self).__init__(**kwargs)
        label = MDFlatButton(text="Wish to leave???", pos_hint={'center_x': .5, 'center_y': 1.5}, font_style='H4')
        button = MDRectangleFlatButton(text="Logout", pos_hint={'center_x': .5, 'center_y': 1}, on_release=self.show)
        self.add_widget(button)
        self.add_widget(label)

    def show(self, obj):
        close_button = MDFlatButton(text='logout', on_release=self.close_button)
        no_button = MDFlatButton(text='No', on_release=self.n_button)
        self.dialog = MDDialog(text='Are u sure u want to logout?', buttons=[close_button, no_button])
        self.dialog.open()

    def close_button(self, LoginScreen):
        self.dialog.dismiss()
        app = MDApp.get_running_app()
        app.root.current = 'login'

    def n_button(self, MenuScreen):
        self.dialog.dismiss()
        app = MDApp.get_running_app()
        app.root.current = 'menu'


class DietRecallApp(MDApp):
    def build(self):
        conn = sqlite3.connect('diet_db.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE if not exists FEEDBACK(feed text)")
        cursor.execute("CREATE TABLE if not exists user_details(email text not null unique primary key, name text, age text,sex text, activity text, weight text,foreign key(email) references user(email) on delete cascade)")
        conn.commit()
        conn.close()
        screen = Builder.load_string(KV)
        screen1 = Screen()
        theme_cls = ThemeManager()
        self.theme_cls.primary_palette = ("Green")
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = ("Light")
        return screen

    def on_switch_active(self, instance_switch, value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

    def get_screen(self, screen_name):
        if screen_name == "feedback":
            return FeedbackScreen()
        else:
            return None


    def show_popup(self):
        conn = sqlite3.connect('diet_db.db')
        cursor = conn.cursor()
        feedback_text = user_feed.text
        cursor.execute("insert into feedback values(?)", (feedback_text,))
        conn.commit()
        conn.close()
        # self.screen_text = ''

        feed_obj.screen_text.text = ''

        toast("Feedback Saved!")
        app = MDApp.get_running_app()
        app.root.current='menu'


    def show_popup1(self):
        # conn = sqlite3.connect('diet_db.db')
        # cursor = conn.cursor()
        # cursor.execute("insert into feedback values(?)",(feedback_text,))
        # conn.commit()
        # conn.close()
        print(email)
        toast("Changes Saved!")
        app = MDApp.get_running_app()
        app.root.current = 'menu'


DietRecallApp().run()




