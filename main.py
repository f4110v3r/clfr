import flet as ft
import requests
import json
def main(page: ft.Page):
    page.title = "Авторизация"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/account",
                [
                    ft.TextField(label="Электронная почта", width=300),
                    ft.TextField(label="Пароль", password=True, width=300),
                    ft.ElevatedButton(text="Войти", on_click=login)
                ],
            )
        )
    def route_change2(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/profile",
                [
                    ft.TextField(label="Электронная почта", width=300),
                    ft.TextField(label="Пароль", password=True, width=300),
                    ft.ElevatedButton(text="Войти", on_click=login)
                ],
            )
        )
        

    # Поля ввода
    email_input = ft.TextField(label="Электронная почта", width=300)
    password_input = ft.TextField(label="Пароль", password=True, width=300)
    localHost='http://172.31.1.203:3000'
    # Кнопка "Войти"
    def login(e):
        email = email_input.value
        password = password_input.value
        if email and password:
            r=requests.post(localHost+"/login", data = {"login":email, "password": password})
            mass = json.loads(r.text)
            print(mass)
            if mass['text'] == "Пользователь авторизориван!":
                page.add(ft.Text(f"Успешный вход как {email}")) 
                page.go("/profile")
                route_change("/profile")
            else: page.add(ft.Text(mass['error'], color=ft.colors.RED))
        else:
            page.add(ft.Text("Пожалуйста, введите электронную почту и пароль", color=ft.colors.RED))

    login_button = ft.ElevatedButton(text="Войти", on_click=login)
    page.add(
        ft.Column(
            controls=[
                email_input,
                password_input,
                login_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )
    
# Запуск приложения
ft.app(target=main)
import flet as ft
import requests
import json
def main(page: ft.Page):
    page.title = "Авторизация"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/account",
                [
                    ft.TextField(label="Электронная почта", width=300),
                    ft.TextField(label="Пароль", password=True, width=300),
                    ft.ElevatedButton(text="Войти", on_click=login)
                ],
            )
        )
    def route_change2(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/profile",
                [
                    ft.TextField(label="Электронная почта", width=300),
                    ft.TextField(label="Привет", password=True, width=300),
                    
                ],
            )
        )
        

    # Поля ввода
    email_input = ft.TextField(label="Электронная почта", width=300)
    password_input = ft.TextField(label="Пароль", password=True, width=300)
    localHost='http://172.31.1.203:3000'
    # Кнопка "Войти"
    def login(e):
        email = email_input.value
        password = password_input.value
        if email and password:
            r=requests.post(localHost+"/login", data = {"login":email, "password": password})
            mass = json.loads(r.text)
            print(mass)
            if mass['text'] == "Пользователь авторизориван!":
                page.add(ft.Text(f"Успешный вход как {email}")) 
                page.go("/profile")
                route_change2("/profile")
            else: page.add(ft.Text(mass['error'], color=ft.colors.RED))
        else:
            page.add(ft.Text("Пожалуйста, введите электронную почту и пароль", color=ft.colors.RED))

    login_button = ft.ElevatedButton(text="Войти", on_click=login)
    page.add(
        ft.Column(
            controls=[
                email_input,
                password_input,
                login_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )
    
# Запуск приложения
ft.app(target=main)