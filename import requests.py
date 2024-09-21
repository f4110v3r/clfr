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
from kivy.uix.label import Label
import json
"""""
localHost='http://172.31.1.203:3000'
r = requests.get(localHost)
print(r.text)

r=requests.post(localHost+"/login", data = {"username":"123", "password": "222"})
print(r.text)
"""
localHost='http://172.31.1.203:3000'
path=r"C:\Users\user\Documents\clfr\clfr\1052.4.jpg"
layout = FloatLayout()
button = Button(text='Войти',font_size=40,background_color=(0,0,0, 1),size_hint =(.3, .10),pos =(672, 300))
layout.add_widget(button)
logininput = TextInput(text='login',font_size=40,size_hint =(.3, .10),pos =(672, 640), multiline=False)
layout.add_widget(logininput)
passinput = TextInput(text='password',font_size=40,size_hint =(.3, .10),pos =(672, 500), multiline=False)
layout.add_widget(passinput)
l = Label(text='Вход',color=(0,0,0,1), font_size='50sp',size_hint =(.3, .10),pos =(672, 780))
l2 = Label(text='',color=(0,0,0,1), font_size='30sp',size_hint =(.3, .10),pos =(672, 400))
layout.add_widget(l)
layout.add_widget(l2)



def on_button_press(instance):
        r=requests.post(localHost+"/login", data = {"login":logininput.text, "password": passinput.text})
        l2.text=r.text
"""""
        button.bind(on_press=self.on_button_press)
    
    def on_button_press(self):
        self.logininput.text = "Спасибо!"
        """
class MyApp(App):
    button.bind(on_press=on_button_press)
    def build(self):
        Window.clearcolor = (255, 255, 255, 1)
        

        return layout
if name == 'main':
    MyApp().run()