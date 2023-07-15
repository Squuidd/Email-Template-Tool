import PySimpleGUI as sg
import json
import window as wd
import os


def templates_path():
    absolute_path = os.path.dirname(__file__)
    relative_path = "Templates/"
    full_path = os.path.join(absolute_path, relative_path)

    return full_path


class Template:
    def __init__(self, name):
        self.name = name
    
    def create_txt(self):
        path = templates_path()
        file = f"{path}/{self.name}.txt"
        
        open(file, "x")

        self.path = file

  

window = wd.main()

def create_template(name):
    window.extend_layout(window['new_column'], wd.template_button(template_name))

    template = Template(name)
    template.create_txt()
    


# scan for templates

select_events = []
edit_events = []

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == "add_template":
        template_name = wd.name_input()
        create_template(template_name)

        select_events.append(f"{template_name}")
        edit_events.append(f"{template_name}")

    for e in edit_events:
        if event == f"{e}_edit":
            path = f"{templates_path()}/{e}.txt"
            os.startfile(path)


window.close()

