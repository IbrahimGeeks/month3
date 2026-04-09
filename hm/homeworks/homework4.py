import flet as ft 
import datetime as dt

now = dt.datetime.now()



def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    greeting_history = []

    chose_history = []

    greeting_text = ft.Text('История заполнения:')

    chose_text = ft.Text('Избранное:')

    def text_name(e):
        name = text_input.value.strip()

        if name:
            if name.isdigit():
                text_hello.value = "Имя не может состоять из цифр!"
                text_hello.color = ft.Colors.RED_900

            elif len(name) < 2:
                text_hello.value = "Имя должно быть не менее 2 символов!"
                text_hello.color = ft.Colors.RED_900

            elif name in greeting_history:
                text_hello.value = "Это имя уже в истории"
                text_hello.color = ft.Colors.RED
            else:
                text_hello.value = f"Привет! {name}"
                text_hello.color = ft.Colors.BLUE
                greeting_history.append(name)
                greeting_text.value = "История приветствия:\n" + "\n".join(greeting_history)

            text_input.value = ""

        else:
            text_hello.value = "Введите корректное имя!"
            text_hello.color = ft.Colors.RED_900


        if len(greeting_history) > 4:
            delete_name(index=0)

        page.update()

    def thememode(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        
        page.update()


    text_hello = ft.Text('Как тебя зовут?', size=20)
    text_input = ft.TextField(label='Ваше имя', on_submit=text_name, expand=False)
    btn = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=text_name)


    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)

    def clear_history(e):
        greeting_history.clear()
        greeting_text.value = "История приветсвия:"
        chose_history.clear()
        chose_text.value = 'Избранное'

    def add_favorite(e):
        name = text_input.value.strip()
        if name:
            chose_history.append(name)
            chose_text.value = f'Избранное: \n' + "\n".join(chose_history)
            text_input.value = ""
        else:
            text_hello.value = "Введите корректное имя!" 
            text_hello.color = ft.Colors.RED_900


    def delete_name(index):
        greeting_history.pop(index)
        
        


    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    chose_button = ft.IconButton(icon=ft.Icons.FAVORITE, on_click=add_favorite)

    main_object = ft.Row(
        controls=[text_input, btn, chose_button],
        alignment=ft.MainAxisAlignment.CENTER
        ) 

    page.add(ft.Column([ ft.Row([clear_button, theme_btn], alignment=ft.MainAxisAlignment.CENTER), text_hello, main_object, greeting_text, chose_text], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER))


ft.app(main_page, view=ft.AppView.WEB_BROWSER) 