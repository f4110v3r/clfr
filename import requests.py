import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0, 0, 0, 1)  # Цвет кнопки
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class RoundedTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Цвет фона поля ввода
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.focus = True
        return super().on_touch_down(touch)

class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # Белый фон
        layout = FloatLayout()

        button = RoundedButton(text='Войти', font_size=40, size_hint=(.3, .1), pos=(672, 300))
        layout.add_widget(button)

        textinput = RoundedTextInput(hint_text='Логин', font_size=40, size_hint=(.3, .1), pos=(672, 500), multiline=False)
        layout.add_widget(textinput)

        textinput1 = RoundedTextInput(hint_text='Пароль', font_size=40, size_hint=(.3, .1), pos=(672, 640), multiline=False)
        layout.add_widget(textinput1)

        return layout

if __name__ == '__main__':
    MyApp().run()
