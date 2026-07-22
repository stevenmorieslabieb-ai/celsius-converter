import flet as ft  

def main(page:ft.Page):
    page.title = "Celsius to Fahrenheit App"
    page.bgcolor = "#FFF9BA"
    page.window.width = 300
    page.window.height = 400
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    screen = ft.TextField(label="write the value of celsius ",text_size=20, width=220 )
    text =ft.Text(size=22)
    please_enter = ft.Text("Please Enter The Value", size=20, color="black", visible= False)
    def converter(e):
        if screen.value.strip() != "":
            num = float(screen.value) *9/5 + 32
            text.value = f"The Value In Fahrenheit Is :{num}"
            page.update()
        else:
            please_enter.visible = True
            page.update()
        

    
    convert_btn = ft.ElevatedButton( "To Fahrenheit",bgcolor="#A0DBF7",on_click=converter)
    page.add(screen,convert_btn,text,please_enter)
ft.app(target=main)