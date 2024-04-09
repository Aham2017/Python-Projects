import flet as ft

def main(page: ft.Page):
    def maker(e):
        with open("thing.txt", "w") as file:
            file.write(str(textbox.value))
                
    def opener(e):
        try:
            with open("thing.txt", "r") as file:
                textbox.value = file.read()
                counter()
        except FileNotFoundError:
            print("Not f0und")

    def recorder(e):
        with open("thing.txt", "w") as file:
            file.write(str(textbox.value))

    def counter(e):
        count.value = f"Words: {len(textbox.value.split())}"
        page.update()

    textbox = ft.TextField(
        value="",
        hint_text="Enter text here",
        multiline=True,
        on_change=counter
    )
    count = ft.Text(value="Current Words: 0")
    openerer = ft.ElevatedButton(text="Open File", on_click=opener)
    save = ft.ElevatedButton(text="Save File", on_click=recorder)
    create = ft.ElevatedButton(text="Create File", on_click=maker)
    page.add(openerer, save, create, textbox, count)

ft.app(target=main)