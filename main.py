import flet as ft
import requests
import json

# Создаем глобальную переменную для хранения информации о пользователе
user_info = {}

def main(page: ft.Page):
    page.title = "Приложение"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE
    
    localHost = 'http://172.31.1.103:3000'
    
    # Функция перехода на страницу профиля
    def route_to_profile():
        page.views.clear()
        page.title = "Личный кабинет"
        page.bgcolor = ft.colors.WHITE
        page.views.append(
            ft.View(
                "/profile",
                [
                    ft.Container(
                        padding=ft.padding.only(left=50, top=50),
                        content=ft.Row(
                            [
                                ft.Container(
                                    content=ft.Image(src=user_info["photo_url"], width=120, height=120, fit=ft.ImageFit.COVER),
                                    width=120,
                                    height=120,
                                    border_radius=60,
                                    bgcolor=ft.colors.GREY_200,
                                    padding=5,
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(f"Имя: {user_info['name']}", color=ft.colors.BLACK, size=24),
                                            ft.Text(f"Логин: {user_info['login']}", color=ft.colors.GREY, size=18, text_align=ft.TextAlign.CENTER),
                                            ft.Text(f"Команда: {user_info['team']}", color=ft.colors.BLACK, size=24)
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=10
                                    ),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                    ),
                    create_bottom_nav(0)
                ],
            )
        )
        page.update()

    # Функция создания докбара
    def create_bottom_nav(selected_index):
        return ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.PERSON, label="Профиль"),
                ft.NavigationDestination(icon=ft.icons.MAP, label="Карта знаний"),
                ft.NavigationDestination(icon=ft.icons.LEADERBOARD, label="Таблица лидеров"),
            ],
            selected_index=selected_index,
            on_change=change_page,
        )
    
    # Функция обработки переходов по страницам
    def change_page(e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            route_to_profile()
        elif selected_index == 1:
            route_to_knowledge_map()
        elif selected_index == 2:
            route_to_leaderboard()
        page.update()

    # Функция перехода на страницу авторизации
    def route_to_authorization():
        page.views.clear()
        page.title = "Авторизация"
        page.bgcolor = ft.colors.WHITE
        page.views.append(
            ft.View(
                "/auth",
                [
                    ft.Column(
                        controls=[
                            email_input,
                            password_input,
                            login_button,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                ],
            )
        )
        page.update()

    # Функция перехода на страницу "Карта знаний"
    def route_to_knowledge_map():
        page.views.clear()
        page.title = "Карта знаний"
        page.bgcolor = ft.colors.WHITE
        page.views.append(
            ft.View(
                "/knowledge_map",
                [
                    ft.Text("Это карта знаний", size=24),
                    create_bottom_nav(1)
                ],
            )
        )
        page.update()

    # Функция перехода на страницу таблицы лидеров
    def route_to_leaderboard():
        page.views.clear()
        page.title = "Таблица лидеров"
        page.bgcolor = ft.colors.WHITE
        
        # Данные для таблицы лидеров
        tt = requests.get(localHost + "/top-teams")
        teams_data = json.loads(tt.text)

        # Создаем таблицу с местами команд
        leaderboard = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Место", weight=ft.FontWeight.BOLD, size=18),
                        ft.Text("Название команды", weight=ft.FontWeight.BOLD, size=18),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                ),
                *[
                    ft.Row(
                        controls=[
                            ft.Text(f"{rank} место", size=16, width=50, text_align=ft.TextAlign.LEFT),
                            ft.Text(teams_data["name"], size=16),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ) for rank, team in zip(["1-е", "2-е", "3-е"], teams_data[:3])
                ]
            ]
        )
        
        page.views.append(
            ft.View(
                "/leaderboard",
                [
                    ft.Column(
                        controls=[
                            ft.Text("Таблица лидеров", size=24, weight=ft.FontWeight.BOLD),
                            leaderboard
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20
                    ),
                    create_bottom_nav(2)
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
                user_info_json = requests.post(localHost + "/userpage", data={"login": email})
                uij = json.loads(user_info_json.text)
                global user_info
                user_info = {
                    "name": uij['name'],
                    "login": email,
                    "photo_url": response.get('photo_url', localHost + uij['avatar']),
                    "team": uij['team']
                }
                route_to_profile()
                
        else:
            page.add(ft.Text("Пожалуйста, введите электронную почту и пароль", color=ft.colors.RED))

    # Поля ввода
    email_input = ft.TextField(label="Электронная почта", width=300)
    password_input = ft.TextField(label="Пароль", password=True, width=300)
    login_button = ft.ElevatedButton(text="Войти", on_click=login)

    # Изначально отображаем страницу авторизации
    route_to_authorization()

# Запуск приложения
ft.app(target=main)
    