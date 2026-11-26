import flet as ft


def main(page: ft.Page):
    page.title = "Название окна"
    page.theme_mode = ft.ThemeMode.DARK

    # Добавляем элемент на страницу
    page.add(ft.Text("Привет, мир!"))


ft.run(main)