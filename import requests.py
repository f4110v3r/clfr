import requests
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
"""""
localHost='http://172.31.1.203:3000'
r = requests.get(localHost)
print(r.text)

r=requests.post(localHost+"/login", data = {"username":"123", "password": "222"})
print(r.text)
"""
path=r"C:\Users\user\Documents\clfr\clfr\1052.4.jpg"
layout = FloatLayout()
button = Button(text='Войти',font_size=40,background_color=(0,0,0, 1),size_hint =(.3, .10),pos =(672, 300))
layout.add_widget(button)
textinput = TextInput(text='login',font_size=40,size_hint =(.3, .10),pos =(672, 500), multiline=False)
layout.add_widget(textinput)
textinput1 = TextInput(text='password',font_size=40,size_hint =(.3, .10),pos =(672, 640), multiline=False)
layout.add_widget(textinput1)


    
    
"""""
class LoginPage(Screen):
    def verify_credentials(self):
        if self.ids["login"].text == "username" and self.ids["passw"].text == "password": #Сережа замени юзернейм и пассворд реквестами на бд это сравнение введённого и хранимого на бд
            self.manager.current = "user"

class UserPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

kv_file = Builder.load_file('login.kv')
"""
class MyApp(App):
    def build(self):
        Window.clearcolor = (255, 255, 255, 1)
        return layout

if __name__ == '__main__':
    MyApp().run()