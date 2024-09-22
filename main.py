import flet as ft
import requests
import json

user_info = {}
selected_branch = None  # Глобальная переменная для хранения выбранной ветки

def main(page: ft.Page):
    global selected_branch  # Указываем, что будем использовать глобальную переменную

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
        

        # Контейнер для участников команды content=ft.Text(f"Команда: {user_info['team']}", color=ft.colors.BLACK, size=24)
        
        members_container = ft.Column(
    controls=[
        
        
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Image(src=localHost+member['avatar'], width=60, height=60, fit=ft.ImageFit.COVER),
                        width=60,
                        height=60,
                        border_radius=30,
                        bgcolor=ft.colors.GREY_200,
                        padding=5,
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(member['name'], color=ft.colors.BLACK, size=16),
                            ft.Text(f"Прогресс: {member['points']}", color=ft.colors.GREY, size=14),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=5
                    ),
                ],
                alignment=ft.MainAxisAlignment.END,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ) for member in teammates
    
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
                ft.NavigationDestination(icon=ft.icons.BOOK,label='Словарь' )
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
        elif selected_index == 3:
            route_to_dict()
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
        global selected_branch
        page.views.clear()
        page.title = "Карта знаний - Пельмени"
        page.bgcolor = ft.colors.WHITE

        # Данные для курса
        branches = {
            "Ветка 1": ["Задание 1.1", "Задание 1.2"],
            "Ветка 2": ["Задание 2.1", "Задание 2.2"],
            "Ветка 3": ["Задание 3.1", "Задание 3.2"],
        }

        # Функция для изменения цвета кружков
        def change_circle_color(branch):
            global selected_branch
            selected_branch = branch
            page.update()

        # Создание кругов для каждой ветки
        branch_circles = []
        for branch_name, tasks in branches.items():
            row = ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(branch_name, color=ft.colors.WHITE, size=14),
                        width=100,
                        height=30,
                        border_radius=15,
                        bgcolor=ft.colors.BLUE if selected_branch == branch_name else ft.colors.GREY,
                        alignment=ft.alignment.center,
                        on_click=lambda e, branch=branch_name: change_circle_color(branch)  # Меняет цвет
                    ),
                    *[
                        ft.Container(
                            content=ft.Text(str(i + 1), color=ft.colors.WHITE, size=20),
                            width=50,
                            height=50,
                            border_radius=25,
                            bgcolor=ft.colors.GREEN if selected_branch == branch_name else ft.colors.GREY,
                            alignment=ft.alignment.center,
                            on_click=lambda e, task=f"{branch_name} - {task}": route_to_task(task),  # Переход на задание
                        ) for i, task in enumerate(tasks)
                    ],
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            )
            branch_circles.append(row)

        page.views.append(
            ft.View(
                "/knowledge_map",
                [
                    ft.Column(
                        controls=[
                            ft.Text("Курс: Пельмени", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            *branch_circles
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    ),
                    create_bottom_nav(1)
                ],
            )
        )
        page.update()
    def route_to_dict():
        page.views.clear()
        page.title = "Словарь"
        page.bgcolor = ft.colors.WHITE
        page.views.append(
            ft.View(
                "/dictionary",
                [
                    ft.Column(
                        controls=[
                            ft.Text("Словарь определений по пельменям", width=300,size=24),
                            ft.Text("Определение 1", width=300,size=10),
                            ft.Text("Определение 2", width=300,size=10),
                            ft.Text("Определение 3", width=300,size=10),


                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                ],
            )
        )
        page.update()
    # Функция для перехода на страницу задания
    def route_to_task(task_name):
        page.views.clear()
        page.title = task_name
        page.bgcolor = ft.colors.WHITE

        # Здесь добавьте контент для страницы задания
        page.views.append(
            ft.View(
                f"/task_{task_name}",
                [
                    ft.Text(f"Это содержание для {task_name}", size=24),
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
                global teammates
                teammates=uij['teammates']
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
