from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDIconButton
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import sqlite3

Builder.load_string("""
<LoginUI>:
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0  
        Rectangle:
            pos: self.pos
            size: self.size

    orientation: 'vertical'
    spacing: '1.338cm'
    padding: '2.04cm'

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: '3.5cm'

        Image:
            source: "domy.jpg"
            size_hint_y: None
            height: "2.0cm"        

        Label:
            text: 'Log In'
            font_size: '1.05833cm'
            color: 0, 0, 0, 1

    BoxLayout:
        orientation: 'vertical'
        spacing: '0.5cm'
        TextInput:
            id: username_input
            multiline: False
            hint_text: "Username"
            size_hint: None, None
            size_hint_x: 1
            height: '1.40cm'
            font_size: '0.635cm'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            padding: self.height / 2 - self.font_size / 2
            required: True

    BoxLayout:
        orientation: 'vertical'
        spacing: '0.5cm'
        TextInput:
            id: password_input
            multiline: False
            size_hint: None, None
            size_hint_x: 1
            height: '1.40cm'
            hint_text: "Password"
            font_size: '0.635cm'
            password:True
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            padding: self.height / 2 - self.font_size / 2
            required: True

        BoxLayout:
            orientation: 'horizontal'

            MDCheckbox:
                size_hint: None, None
                size_hint_x: None
                size_hint_y: None
                width: '23dp'
                height: '10dp'
                color: 0,0,0, 1

            Label:
                text: 'Remember Me'
                font_size: '0.5cm'
                size_hint_x: None
                width: '5cm'
                color: app.theme_cls.primary_color

    MDRaisedButton:
        id: login_button
        size_hint: None, None
        size_hint_x: 1
        size_hint_y: 1
        height: '1.549cm'
        text: 'Log In'
        font_size: '0.635cm'
        pos_hint: {'center_y': 0.9}
        on_press: root.check_fields_login()

    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: '0.2cm'

        Label:
            text: 'Reset Password'
            font_size: '0.56444401cm'
            color: app.theme_cls.primary_color
            size_hint_x: None
            size_hint_y: 1
            width: '7cm'
            underline: True
            on_touch_down:
                if self.collide_point(*args[1].pos): app.root.current = "resetpassword"

    BoxLayout:
        orientation: 'horizontal'
        height: '0.2cm'
        Label:
            text: 'Not a user yet?'
            font_size: '0.6cm'
            align: 'left'
            size_hint_x: None
            size_hint_y: 2
            width: '3cm'
            color: 0, 0, 0, 1

        Label:
            text: 'Create Account'
            font_size: '0.56444401cm'
            color: 0, 1, 1, 1
            size_hint_x: None
            size_hint_y: 2
            width: '5cm'
            underline: True
            color: app.theme_cls.primary_color
            on_touch_down:
                if self.collide_point(*args[1].pos): app.root.current = "signup"
""")

Builder.load_string("""
<SignUpUI>:
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0  
        Rectangle:
            pos: self.pos
            size: self.size
    orientation: 'vertical'
    spacing: '1.338cm'
    padding: '2.04cm'

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: '4.5cm'

        Image:
            source: "domy.jpg"
            size_hint_y: None
            height: "2.465cm"

        Label:
            text: 'Sign Up'
            font_size: '1.05833cm'
            color: 0, 0, 0, 1

    BoxLayout:
        orientation: 'vertical'
        spacing: '0.5cm'  
        TextInput:
            id: email_input
            multiline: False
            hint_text: "Email"  
            size_hint: None, None
            size_hint_x: 1
            height: '1.50cm'
            font_size: '0.635cm'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            padding: self.height / 2 - self.font_size / 2

        TextInput:
            id: password_input
            multiline: False
            hint_text: "Password"
            size_hint: None, None
            size_hint_x: 1
            height: '1.549cm'
            font_size: '0.635cm'
            password: True
            padding: self.height / 2 - self.font_size / 2

        TextInput:
            id: confirm_password_input
            multiline: False
            hint_text: "Confirm Password"
            size_hint: None, None
            size_hint_x: 1
            height: '1.549cm'
            font_size: '0.635cm'
            password: True
            padding: self.height / 2 - self.font_size / 2

    MDRaisedButton:
        size_hint: None, None
        size_hint_x: 1
        height: '1.549cm'
        text: 'Register'
        font_size: '0.635cm'
        pos_hint: {'center_x': 0.5}
        on_press: root.check_fields()
""")
Builder.load_string("""

<ResetPasswordUI>:
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0 
        Rectangle:
            pos: self.pos
            size: self.size
    orientation: 'vertical'
    spacing: '1.338cm'
    padding: '2.04cm'

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: '4.5cm'  

        Label:
            text: 'Reset Password'
            font_size: '1.05833cm'
            color: 0, 0, 0, 1

    BoxLayout:
        orientation: 'vertical'
        spacing: '0.5cm'  
        TextInput:
            id: email_input
            multiline: False
            hint_text: "Email"
            size_hint: None, None
            size_hint_x: 1
            height: '1.50cm'
            font_size: '0.635cm'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            padding: self.height / 2 - self.font_size / 2

    BoxLayout:
        orientation: 'vertical'
        spacing: '0.5cm'  
        TextInput:
            id: new_input
            multiline: False
            size_hint: None, None
            size_hint_x: 1
            height: '1.549cm'
            hint_text: "New Password"
            font_size: '0.635cm'
            password: True
            padding: self.height / 2 - self.font_size / 2

    BoxLayout:
        orientation: 'vertical'
        spacing: '0.5cm'  
        TextInput:
            id: confirm_input
            multiline: False
            size_hint: None, None
            size_hint_x: 1
            height: '1.549cm'
            hint_text: "Confirm Password"
            font_size: '0.635cm'
            password: True
            padding: self.height / 2 - self.font_size / 2

    MDRaisedButton:
        size_hint: None, None
        size_hint_x: 1
        height: '1.549cm'
        text: 'Submit'
        font_size: '0.635cm'
        pos_hint: {'center_x': 0.5}
        on_press: root.check_fields2()

    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: '0.2cm'

        Label:
            text: 'Back to login'
            font_size: '0.56444401cm'
            color: app.theme_cls.primary_color
            size_hint_x: None
            width: '7cm'
            underline: True
            on_touch_down:
                if self.collide_point(*args[1].pos): app.root.current = "login"             
""")

Builder.load_string("""
<ImageUi>:
    Image:
        source: 'GET_STARTED_2.jpg'
        size: root.width, root.height
        allow_stretch: True
        keep_ratio: False

    MDRaisedButton:
        text: "Continue"
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        size_hint: (0.4, 0.0)
        font_size: '20sp'
        underline: False
        on_touch_down:
            if self.collide_point(*args[1].pos): app.root.current = "Diet"
            else: self.underline = False

        on_touch_up:
            self.underline = False

""")

Builder.load_string('''
<DietUI>:
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0  
        Rectangle:
            pos: self.pos
            size: self.size
    orientation: 'vertical'
    spacing: '1.338cm'
    padding: '2.04cm'

    MDLabel:
        text: 'Choose your Diet'
        font_size: '40sp'
        halign: 'center'
        color: 0, 0, 0, 1
        size_hint_y: None
        height: '5cm'

    BoxLayout:
        orientation: 'vertical'
        spacing: '0.8cm'  
        MDRectangleFlatButton:
            id: balanced_diet_button
            text: 'Balanced Diet'
            font_size: '0.635cm'
            size_hint: None, None
            size_hint_x: 1
            height: '1.549cm'
            md_bg_color: (1, 1, 1, 1)  
            on_release: root.set_button_color(balanced_diet_button)

        MDRectangleFlatButton:
            id: keto_diet_button
            text: 'Keto Diet'
            font_size: '0.635cm'
            size_hint: None, None
            size_hint_x: 1
            height: '1.549cm'
            md_bg_color: (1, 1, 1, 1)  
            on_release: root.set_button_color(keto_diet_button)

        MDRectangleFlatButton:
            id: friendly_diet_button
            text: 'Friendly Diet'
            font_size: '0.635cm'
            size_hint: None, None
            size_hint_x: 1
            height: '1.549cm'
            md_bg_color: (1, 1, 1, 1)  
            on_release: root.set_button_color(friendly_diet_button)

        MDRaisedButton:
            size_hint: None, None
            size_hint_x: 1
            height: dp(20)
            text: 'Next'
            font_size: '0.635cm'
            pos_hint:{'center_x':0.5}
            on_press: root.check_diet_selection()

''')

Builder.load_string('''
<GenderUI>:
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0  
        Rectangle:
            pos: self.pos
            size: self.size
    orientation: 'vertical'
    spacing: '1.338cm'
    padding: '2.04cm'

    MDLabel:
        text: 'What is your Gender?'
        font_size: '40sp'
        halign: 'center'
        color: 0, 0, 0, 1
        size_hint_y: None
        height: '5cm'

    BoxLayout:
        orientation: 'vertical'
        spacing: '0.8cm'  
        MDRectangleFlatButton:
            id: male_button
            text: 'Male'
            font_size: '0.635cm'
            size_hint: None, None
            size_hint_x: 1
            height: '1.549cm'
            md_bg_color: (1, 1, 1, 1)   
            on_release: root.set_button_color(male_button)

        MDRectangleFlatButton:
            id: female_button
            text: 'Female'
            font_size: '0.635cm'
            size_hint: None, None
            size_hint_x: 1
            height: '1.549cm'
            md_bg_color: (1, 1, 1, 1)  
            on_release: root.set_button_color(female_button)

        MDRectangleFlatButton:
            id: other_button
            text: 'Others'
            font_size: '0.635cm'
            size_hint: None, None
            size_hint_x: 1
            height: '1.549cm'
            md_bg_color: (1, 1, 1, 1) 
            on_release: root.set_button_color(other_button)

        MDRaisedButton:
            size_hint: None, None
            size_hint_x: 1
            height: dp(50)
            text: 'Continue'
            font_size: '0.635cm'
            pos_hint:{'center_x':0.5}
            on_press: root.check_gender_selection()

    BoxLayout:
        size_hint_y: None
        height: '0.2cm'
        Label:
            text: 'Back'
            font_size: '0.56444401cm'
            color: app.theme_cls.primary_color
            size_hint_x: None
            width: '7cm'
            underline: True
            on_touch_down:
                if self.collide_point(*args[1].pos): app.root.current = "Diet"
''')

Builder.load_string("""
<DateOfBirthUI>:
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0  
        Rectangle:
            pos: self.pos
            size: self.size
    orientation: 'vertical'
    padding: '1cm'
    pos_hint: {'top': 1}  

    Image:
        source: "date-of-birth.jpg"
        size_hint_y: None
        height: dp(100)
        allow_stretch: True
        keep_ratio: True

    MDLabel:
        text: 'Enter your Date of Birth'
        font_size: '40sp'
        halign: 'center'
        size_hint_y: None
        height: dp(100)

    BoxLayout:
        orientation: 'horizontal'
        spacing: '0.2cm'  
        size_hint_y: None
        height: dp(150)

        TextInput:
            multiline: False
            hint_text: "dd"  
            size_hint: None, None
            size_hint_x: 1
            height: dp(50)
            font_size: '0.635cm'
            id: day_input

        TextInput:
            multiline: False
            hint_text: "mm"  
            size_hint: None, None
            size_hint_x: 1
            height: dp(50)
            font_size: '0.635cm'
            id: month_input

        TextInput:
            multiline: False
            hint_text: "yyyy"  
            size_hint: None, None
            size_hint_x: 1
            height: dp(50)
            font_size: '0.635cm'
            id: year_input         

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: dp(100)

        MDRaisedButton:
            size_hint: None, None
            size_hint_x: 0.5
            height: dp(50)
            text: 'Continue'
            font_size: '0.635cm'
            pos_hint:{'center_x':0.5}
            on_press: root.check_fields()

    BoxLayout:
        size_hint_y: None
        height: '3.5cm'
        Label:
            text: 'Back'
            font_size: '0.7cm'
            color: app.theme_cls.primary_color
            size_hint_x: 0.1
            width: '7cm'
            underline: True
            on_touch_down:
                if self.collide_point(*args[1].pos): app.root.current = "Gender"  

""")

Builder.load_string("""

<ActivityLevelUI>:

    canvas.before:
        Color:
            rgba: 0, 0, 0, 0  
        Rectangle:
            pos: self.pos
            size: self.size
    orientation:'vertical'
    spacing:'20dp'
    padding:'60dp'
    MDLabel:
        text: 'What is your Activity Level?'
        font_size: '30sp'
        align: 'center'
        color: 0, 0, 0, 1
        size_hint_y: None
        height: '3cm'

    BoxLayout:
        orientation: 'vertical'
        spacing: '0.5cm'  
        MDRectangleFlatButton:
            id: no_activity_button
            text: 'No Activity'
            font_size: '0.635cm'
            size_hint: None, None
            size_hint_x: 1
            height: '1.549cm'
            md_bg_color: (1, 1, 1, 1) 
            on_release: root.set_button_color(no_activity_button)

    BoxLayout:
        orientation: 'vertical'
        spacing: '0.5cm'  
        MDRectangleFlatButton:
            id: light_activity_button
            text: 'Light Activity'
            font_size: '0.635cm'
            size_hint: None, None
            size_hint_x: 1
            height: '1.549cm'
            md_bg_color: (1, 1, 1, 1)
            on_release: root.set_button_color(light_activity_button)

    BoxLayout:
        orientation: 'vertical'
        spacing: '0.1cm'  
        MDRectangleFlatButton:
            id: medium_activity_button
            text: 'Medium Activity'
            font_size: '0.635cm'
            size_hint: None, None
            size_hint_x: 1
            height: '1.549cm'
            md_bg_color: (1, 1, 1, 1)
            on_release: root.set_button_color(medium_activity_button)

    BoxLayout:
        orientation: 'vertical'
        spacing: '0.5cm'  
        MDRectangleFlatButton:
            id: heavy_activity_button
            text: 'Heavy Activity'
            font_size: '0.635cm'
            size_hint: None, None
            size_hint_x: 1
            height: '1.549cm'
            md_bg_color: (1, 1, 1, 1)
            on_release: root.set_button_color(heavy_activity_button)

    MDRaisedButton:
        size_hint: None, None
        size_hint_x: 1
        height: dp(40)
        text: 'Next'
        font_size: '0.635cm'
        pos_hint:{'center_x':0.5}
        on_press: root.activity_selection()

    BoxLayout:
        size_hint_y: None
        height: '0.4cm'
        Label:
            text: 'Back'
            font_size: '0.7cm'
            color: app.theme_cls.primary_color
            size_hint_x: 0.5
            width: '15cm'
            underline: True
            on_touch_down:
                if self.collide_point(*args[1].pos): app.root.current = "Dob"

""")

Builder.load_string("""
<HeightUI>:
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0  
        Rectangle:
            pos: self.pos
            size: self.size

    orientation: 'vertical'
    padding: '1cm'
    pos_hint: {'top': 1}  

    Image:
        source: "height.jpg"
        size_hint_y: None
        height: dp(150)
        allow_stretch: True
        keep_ratio: True

    MDLabel:
        text: 'What is your Height?'
        font_size: '40sp'
        halign: 'center'
        size_hint_y: None
        height: dp(100)

    BoxLayout:
        orientation: 'horizontal'
        spacing: '0.2cm'
        size_hint_y: None
        height: dp(150)

        TextInput:
            multiline: False
            hint_text: "Height (in feet)"
            size_hint: None, None
            size_hint_x: 1
            height: dp(50)
            font_size: '0.635cm'
            id: height_input

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: dp(100)

        MDRaisedButton:
            size_hint: None, None
            size_hint_x: 0.8
            height: dp(50)
            text: 'Continue'
            font_size: '0.635cm'
            pos_hint:{'center_x':0.5}
            on_press: root.height_inputting()

    BoxLayout:
        size_hint_y: None
        height: '3.5cm'

        Label:
            text: 'Back'
            font_size: '0.7cm'
            color: app.theme_cls.primary_color
            size_hint_x: 0.1
            width: '7cm'
            underline: True
            on_touch_down:
                if self.collide_point(*args[1].pos): app.root.current = "activity"

""")

Builder.load_string("""
<WeightUI>:
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0  
        Rectangle:
            pos: self.pos
            size: self.size

    orientation: 'vertical'
    padding: '1cm'
    pos_hint: {'top': 1}  

    Image:
        source: "weight.jpg"
        size_hint_y: None
        height: dp(100)
        allow_stretch: True
        keep_ratio: True

    MDLabel:
        text: 'What is your Weight?'
        font_size: '40sp'
        halign: 'center'
        size_hint_y: None
        height: dp(100)

    BoxLayout:
        orientation: 'horizontal'
        spacing: '0.2cm'
        size_hint_y: None
        height: dp(150)

        TextInput:
            id: weight_input
            multiline: False
            hint_text: "Weight (in Kg)"
            size_hint: None, None
            size_hint_x: 1
            height: dp(50)
            font_size: '0.635cm'

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: dp(100)

        MDRaisedButton:
            size_hint: None, None
            size_hint_x: 0.8
            height: dp(50)
            text: 'Continue'
            font_size: '0.635cm'
            pos_hint:{'center_x':0.5}
            on_press:root.weight_inputting()

    BoxLayout:
        size_hint_y: None
        height: '3.5cm'

        Label:
            text: 'Back'
            font_size: '0.7cm'
            color: app.theme_cls.primary_color
            size_hint_x: 0.1
            width: '7cm'
            underline: True
            on_touch_down:
                if self.collide_point(*args[1].pos): app.root.current = "height"

""")


class ActivityLevelUI(MDBoxLayout):
    selected_button = None

    def set_button_color(self, clicked_button):
        for button in self.ids.values():
            if isinstance(button, MDRectangleFlatButton):
                if button == clicked_button:
                    button.md_bg_color = (0, 0.7, 1, 1)
                    button.text_color = (1, 1, 1, 1)
                    self.selected_button = button
                else:
                    button.md_bg_color = (1, 1, 1, 1)
                    button.text_color = (0, 0, 0, 1)

    def activity_selection(self):
        if not self.selected_button:
            popup = Popup(title='Alert',
                          content=Label(text='Please choose your ActivityLevel', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(300, 150))
            popup.open()
        else:
             # making inputted activity level global so later
            # we can use in other functions to store in db.
            global user_activity_level
            user_activity_level = self.selected_button.text

            app = MDApp.get_running_app()
            app.root.current = "height"


class HeightUI(BoxLayout):

    def height_inputting(self):
        height_input = self.ids.height_input

        if not height_input.text:
            popup = Popup(title='Alert',
                          content=Label(text='Please enter your height', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(300, 150))
            popup.open()
            return

        try:
            height = float(height_input.text)
        except ValueError:
            popup = Popup(title='Alert',
                          content=Label(text='**Enter a valid height', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(400, 150))
            popup.open()
            return

        if not (3.0 <= height <= 9.0):
            popup = Popup(title='Alert',
                          content=Label(text='**Enter valid height (between 3.0 and 9.0 feet)', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(450, 200))
            popup.open()
            return

        # making inputted height global so later
            # we can use in other functions to store in db.
        global user_height
        user_height = height

        app = MDApp.get_running_app()
        app.root.current = "weight"


class WeightUI(BoxLayout):

    def weight_inputting(self):
        weight_input = self.ids.weight_input

        if not weight_input.text:
            popup = Popup(title='Alert',
                          content=Label(text='Please enter your weight', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(300, 150))
            popup.open()
            return

        try:
            weight = float(weight_input.text)
        except ValueError:
            popup = Popup(title='Alert',
                          content=Label(text='**Enter a valid weight', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(400, 150))
            popup.open()
            return

        else:
            # making inputted weight global so later
            # we can use in other functions to store in db.
            global user_weight
            user_weight = weight

            """
            this section is the last part after entering email, pass & other inputs
            so here, at this point we will have all the values now we have to
            store all the values in db.. before going back to login.
            """
            conn = sqlite3.connect('diet_db.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (user_email, user_pass, user_height, user_weight, user_gender, user_diet, user_dob, user_activity_level))
            conn.commit()
            conn.close()


        app = MDApp.get_running_app()
        app.root.current = "login"

class DateOfBirthUI(BoxLayout):
    def check_fields(self):
        day_input = self.ids.day_input
        month_input = self.ids.month_input
        year_input = self.ids.year_input

        day_text = day_input.text
        month_text = month_input.text
        year_text = year_input.text

        if not (day_text and month_text and year_text):
            popup = Popup(title='Alert',
                          content=Label(text='**All fields are necessary', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(300, 150))
            popup.open()
            return

        if not (day_text.isdigit() and month_text.isdigit() and year_text.isdigit()):
            popup = Popup(title='Alert',
                          content=Label(text='**Enter numeric values for dd, mm, and yyyy', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(400, 150))
            popup.open()
            return

        day = int(day_text)
        month = int(month_text)
        year = int(year_text)

        if not (1 <= day <= 31) or not (1 <= month <= 12) or not (len(year_text) == 4) or year > 2024:
            popup = Popup(title='Alert',
                          content=Label(text='**Enter a valid date of birth', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(450, 200))
            popup.open()

        else:
            # making inputted DOB global so later
            # we can use in other functions to store in db.
            global user_dob
            user_dob = "-".join([day_text, month_text, year_text]) #"dd-mm-yyyy" format str to store in db text field

            app = MDApp.get_running_app()
            app.root.current = "activity"

    def _init_(self, **kwargs):
        super(DateOfBirthUI, self)._init_(**kwargs)
        self.orientation = 'vertical'
        self.padding = ('1cm', '2cm')
        self.pos_hint = {'top': 1}


class DateOfBirthApp(MDApp):
    def build(self):
        return DateOfBirthUI()


class ResetPasswordUI(BoxLayout):
    def check_fields2(self):
        email_input = self.ids.email_input
        new_input = self.ids.new_input
        confirm_input = self.ids.confirm_input

        if not email_input.text or not new_input.text or not confirm_input.text:
            popup = Popup(title='Alert',
                          content=Label(text='**All fields are mandatory', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(300, 150))
            popup.open()

        elif email_input.text and not email_input.text.endswith("@gmail.com"):
            popup = Popup(title='Alert',
                          content=Label(text='**Please enter a valid email address ', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(400, 150))
            popup.open()

        elif new_input.text != confirm_input.text:
            popup = Popup(title='Alert',
                          content=Label(text='**Passwords do not match', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(300, 150))
            popup.open()

        else:
            global user_up
            email_1=email_input.text
            user_up=new_input.text
            toast("Password Reset successful")
            conn = sqlite3.connect('diet_db.db')
            cursor = conn.cursor()
            cursor.execute("update user set password=?where email=?",(user_up ,email_1))
            conn.commit()
            conn.close()
            app = MDApp.get_running_app()
            app.root.current = "login"
class ImageUi(Screen):
    pass


class DietUI(MDBoxLayout):
    selected_button = None

    def set_button_color(self, clicked_button):
        for button in self.ids.values():
            if isinstance(button, MDRectangleFlatButton):
                if button == clicked_button:
                    button.md_bg_color = (0, 0.7, 1, 1)
                    button.text_color = (1, 1, 1, 1)
                    self.selected_button = button
                else:
                    button.md_bg_color = (1, 1, 1, 1)
                    button.text_color = (0, 0, 0, 1)

    def check_diet_selection(self):
        if not self.selected_button:
            popup = Popup(title='Alert',
                          content=Label(text='**Please choose your Diet', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(300, 150))
            popup.open()
        else:
            # making inputted diet global so later
            # we can use in other functions to store in db.
            global user_diet
            user_diet = self.selected_button.text


            app = MDApp.get_running_app()
            app.root.current = "Gender"


class GenderUI(MDBoxLayout):
    selected_button = None

    def set_button_color(self, clicked_button):
        for button in self.ids.values():
            if isinstance(button, MDRectangleFlatButton):
                if button == clicked_button:
                    button.md_bg_color = (0, 0.7, 1, 1)
                    button.text_color = (1, 1, 1, 1)
                    self.selected_button = button
                else:
                    button.md_bg_color = (1, 1, 1, 1)
                    button.text_color = (0, 0, 0, 1)

    def check_gender_selection(self):
        if not self.selected_button:
            popup = Popup(title='Alert',
                          content=Label(text='**Please choose your Gender', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(300, 150))
            popup.open()
        else:
            # making inputted gender global so later
            # we can use in other functions to store in db.
            global user_gender
            user_gender = self.selected_button.text

            app = MDApp.get_running_app()
            app.root.current = "Dob"


class LoginUI(BoxLayout):
    def check_fields_login(self):
        global user
        username_input = self.ids.username_input
        password_input = self.ids.password_input

        if not username_input.text or not password_input.text:
            popup = Popup(title='Alert',
                          content=Label(text='**All fields are mandatory', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(300, 150))
            popup.open()

        else:

            conn = sqlite3.connect('diet_db.db')
            cursor = conn.cursor()
            username = username_input.text
            password = password_input.text
            cursor.execute("SELECT * FROM user WHERE email=? AND password=?", (username, password))
            user = cursor.fetchone()
            conn.close()
            if user:
                app = MDApp.get_running_app()
                print(self.proceed())
            else:
                popup = Popup(title='Alert',
                              content=Label(text='Invalid username or password', color=(1, 0, 0, 1)),
                              size_hint=(None, None), size=(300, 150))
                popup.open()
        # self.values line 
        self.values = user
        # method proceed used to access the variable 
        def proceed(self):
            global usr_obj
            usr_obj = self
            email_give = usr_obj
            return email_give


class SignUpUI(BoxLayout):
    def check_fields(self):
        email_input = self.ids.email_input
        password_input = self.ids.password_input
        confirm_password_input = self.ids.confirm_password_input

        if not email_input.text and not password_input.text and not confirm_password_input.text:

            popup = Popup(title='Alert',
                          content=Label(text='**All fields are mandatory', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(300, 150))
            popup.open()
        elif email_input.text and not email_input.text.endswith("@gmail.com"):

            popup = Popup(title='Alert',
                          content=Label(text='**Please enter a valid email address ', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(400, 150))
            popup.open()

        elif not email_input.text or not password_input.text or not confirm_password_input.text:
            popup = Popup(title='Alert',
                          content=Label(text='**All fields are mandatory', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(300, 150))
            popup.open()

        elif password_input.text != confirm_password_input.text:
            popup = Popup(title='Alert',
                          content=Label(text='**Passwords do not match', color=(1, 0, 0, 1)),
                          size_hint=(None, None), size=(300, 150))
            popup.open()

        else:
            global user_email, user_pass
            user_email = email_input.text
            user_pass = password_input.text
            app = MDApp.get_running_app()
            app.root.current = 'Image'
class LoginApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Light"
        conn = sqlite3.connect('diet_db.db')
        cursor = conn.cursor()
        cursor.execute("""create table if not exists user(email TEXT PRIMARY KEY UNIQUE NOT NULL,
        password TEXT NOT NULL,
        height REAL,
        weight REAL,
        sex TEXT,
        diettype TEXT,
        dob TEXT,
        activity TEXT )""")
        conn.commit()
        conn.close()
        sm = ScreenManager()
        login_screen = Screen(name='login')
        signup_screen = Screen(name='signup')
        resetpassword_screen = Screen(name='resetpassword')
        image_screen = Screen(name='Image')
        diet_screen = Screen(name='Diet')
        gender_screen = Screen(name='Gender')
        Dob_screen = Screen(name='Dob')
        activity_screen = Screen(name='activity')
        height_screen = Screen(name='height')
        weight_screen = Screen(name='weight')
        login_screen.add_widget(LoginUI())
        signup_screen.add_widget(SignUpUI())
        resetpassword_screen.add_widget(ResetPasswordUI())
        diet_screen.add_widget(DietUI())
        image_screen.add_widget(ImageUi())
        gender_screen.add_widget(GenderUI())
        Dob_screen.add_widget(DateOfBirthUI())
        activity_screen.add_widget(ActivityLevelUI())
        height_screen.add_widget(HeightUI())
        weight_screen.add_widget(WeightUI())
        sm.add_widget(login_screen)
        sm.add_widget(signup_screen)
        sm.add_widget(resetpassword_screen)
        sm.add_widget(image_screen)
        sm.add_widget(diet_screen)
        sm.add_widget(gender_screen)
        sm.add_widget(Dob_screen)
        sm.add_widget(activity_screen)
        sm.add_widget(height_screen)
        sm.add_widget(weight_screen)
        return sm


if __name__ == '__main__':
    login = LoginApp()
    Window.size = (397, 697)
    login.run()
