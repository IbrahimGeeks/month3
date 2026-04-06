import flet as ft


def main(page: ft.Page):
    page.title = "Проверка возраста"

    text_input = ft.TextField(label="Введите возраст")
    result_text = ft.Text()

    def check_age(e):
        value = text_input.value.strip()

        if value == "" or not value.isdigit():
            result_text.value = "Введите корректный возраст"
            result_text.color = ft.Colors.YELLOW

        else:
            age = int(value)

            if age >= 18:
                result_text.value = "Доступ разрешен"
                result_text.color = ft.Colors.GREEN
            else:
                result_text.value = "Доступ запрещен"
                result_text.color = ft.Colors.RED

        page.update()

    button = ft.ElevatedButton("Проверить", on_click=check_age)

    page.add(text_input, button, result_text)


ft.app(main)