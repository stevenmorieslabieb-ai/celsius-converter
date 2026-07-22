

import flet as ft  # type: ignore

def main(page:ft.Page):
    page.title = "Tasks manager"
    page.bgcolor = "#87A6D6"
    page.window.width = 400
    page.scroll = ft.ScrollMode.AUTO
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.resizable = False


    task_input = ft.TextField(label="Write you task",
                               width=150,border_color="#0F154B",
                               border_radius=10,bgcolor="#FFFFFF",
                                color="black",
                                label_style = ft.TextStyle(color="#1F4350"))
    
    tasks_list = ft.Column()
    please_enter = ft.Text("Please Enter The Task", size=20, color="black", visible= False)

    def add_task(e):
        
        if task_input.value.strip() != "":
            new_task_checkbox = ft.Checkbox()
            new_task_text = ft.Text(task_input.value,size=23, color="black")
            def toggle_task(e):
                if new_task_checkbox.value:
                    new_task_text.style =ft.TextStyle(decoration= ft.TextDecoration.LINE_THROUGH,weight=ft.FontWeight.BOLD)
                else:
                    new_task_text.style = None
                    page.update()
           
            new_task_checkbox.on_change = toggle_task
            task_input.value = ""
            new_task = ft.Row([new_task_text, new_task_checkbox])
            tasks_list.controls.append(new_task)
            please_enter.visible = False
            
            def delete_task(e):
                tasks_list.controls.remove(new_task)
                page.update()
            Delete_buttun = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete_task)
            new_task.controls.append(Delete_buttun)
            page.update()
        else:
            please_enter.visible = True
            page.update()
    
    buttun =ft.ElevatedButton("Save", on_click=add_task, bgcolor= "#EBFF83",color="black")

    page.add(task_input,buttun, tasks_list, please_enter, )
ft.app(target=main)