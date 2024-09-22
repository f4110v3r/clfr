import flet as ft
import requests
import json

def main(page: ft.Page):
    page.title = "Авторизация"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE
    
    # Поля ввода
    email_input = ft.TextField(label="Электронная почта", width=300)
    password_input = ft.TextField(label="Пароль", password=True, width=300)
    
    localHost = 'http://172.31.1.203:3000'
    
    # Функция перехода на страницу профиля
    def route_to_profile(user_info):
        page.views.clear()
        page.title = "Личный кабинет"
        page.bgcolor = ft.colors.WHITE
        page.views.append(
            ft.View(
                "/profile",
                [
                    ft.Container(
                        padding=ft.padding.only(left=50, top=50),  # Отступы для сдвига вниз и вправо
                        content=ft.Row(
                            [
                                # Фото профиля в круге
                                ft.Container(
                                    content=ft.Image(src=user_info["photo_url"], width=120, height=120, fit=ft.ImageFit.COVER),
                                    width=120,
                                    height=120,
                                    border_radius=60,  # Делаем круг
                                    bgcolor=ft.colors.GREY_200,  # Цвет фона для фото
                                    padding=5,  # Отступ внутри контейнера для границ
                                ),
                                
                                # Имя и логин справа от фото
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            # Имя пользователя
                                            ft.Text(f"Имя: {user_info['name']}", color=ft.colors.BLACK, size=24),
                                            
                                            # Логин пользователя, меньшего размера и отцентрован
                                            ft.Text(
                                                f"Логин: {user_info['login']}", 
                                                color=ft.colors.GREY, 
                                                size=18, 
                                                text_align=ft.TextAlign.CENTER,
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,  # Центровка текста относительно фото
                                        spacing=10  # Расстояние между именем и логином
                                    ),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,  # Выравнивание ряда по левому краю
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Вертикальная центровка изображения и текста
                        )
                    )
                ],
            )
        )
        page.update()

    # Кнопка "Войти"
    def login(e):
        email = email_input.value
        password = password_input.value
        if email and password:
            r = requests.post(localHost + "/login", data={"login": email, "password": password})
            response = json.loads(r.text)
            if response['text'] == "Пользователь авторизориван!":
                # Получаем информацию о пользователе
                user_info_json = requests.post(localHost + "/userpage", data={"login": email})
                print(user_info_json)
                uij = json.loads(user_info_json.text)
                user_info = {
                    "name": uij['name'],
                    "login": email,
                    "photo_url": response.get('photo_url', 'https://via.placeholder.com/100')  # Заглушка на случай отсутствия фото
                }
                
                # Переход на страницу профиля
                route_to_profile(user_info)
                
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
