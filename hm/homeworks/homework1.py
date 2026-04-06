import flet as ft

def main(page: ft.Page):
    page.title = "Счётчик"

    count = 0
    label = ft.Text(value="Нажато: 0 раз")

    def on_click(e):
        nonlocal count
        count += 1
        label.value = f"Нажато: {count} раз"
        page.update()  
    button = ft.ElevatedButton("Нажми меня", on_click=on_click)

    page.add(label, button)

ft.app(target=main)