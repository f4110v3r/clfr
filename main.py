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

        # Пример данных участников команды
        team_members = [
            {"name": "Участник 1", "photo_url": "url_участника_1", "progress": "50%"},
            {"name": "Участник 2", "photo_url": "url_участника_2", "progress": "70%"},
        ]

        # Контейнер для участников команды content=ft.Text(f"Команда: {user_info['team']}", color=ft.colors.BLACK, size=24)
        
        members_container = ft.Column(
    controls=[
        
        
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Image(src=member["photo_url"], width=60, height=60, fit=ft.ImageFit.COVER),
                        width=60,
                        height=60,
                        border_radius=30,
                        bgcolor=ft.colors.GREY_200,
                        padding=5,
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(member["name"], color=ft.colors.BLACK, size=16),
                            ft.Text(f"Прогресс: {member['progress']}", color=ft.colors.GREY, size=14),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=5
                    ),
                ],
                alignment=ft.MainAxisAlignment.END,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ) for member in team_members
    
    ],
    spacing=10
)


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
                    ft.Container(
                        padding=ft.padding.only(right=20, bottom=20),
                        content=members_container
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

        # Пример данных с заданиями
        tasks = [
            {"number": 1, "title": "Задание 1"},
            {"number": 2, "title": "Задание 2"},
            {"number": 3, "title": "Задание 3"},
            {"number": 4, "title": "Задание 4"},
        ]

        task_circles = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text(str(task["number"]), color=ft.colors.WHITE, size=20),
                    width=50,
                    height=50,
                    border_radius=25,
                    bgcolor=ft.colors.BLUE,
                    alignment=ft.alignment.center,
                    on_click=lambda e: route_to_task(task["number"]),  # Переход на страницу задания
                ) for task in tasks
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )

        page.views.append(
            ft.View(
                "/knowledge_map",
                [
                    ft.Column(
                        controls=[
                            ft.Text("Карта учебного курса", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            task_circles
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    ),
                    create_bottom_nav(1)
                ],
            )
        )
    page.update()

    def route_to_task(task_number):
        page.views.clear()
        page.title = f"Задание {task_number}"
        page.bgcolor = ft.colors.WHITE

        # Здесь добавьте контент для страницы задания
        page.views.append(
            ft.View(
                f"/task_{task_number}",
                [
                    ft.Text(f"Это содержание задания {task_number}", size=24),
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
                            ft.Text(team['name'], size=16),
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
