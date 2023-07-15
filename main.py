import PySimpleGUI as sg
import json
import window as wd
import os
import pyperclip


select_events = []
edit_events = []

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
        self.save()

    def save(self):
        with open("config.json", 'r') as f:
            data = json.load(f)
        data["Templates"].append([self.name, self.path])

        with open("config.json", "w") as f:
            json.dump(data, f)

def load_templates():
    with open("config.json", 'r') as f:
        data = json.load(f)

    for i in data["Templates"]:
        select_events.append(i[0])
        edit_events.append(i[0])  
        print(i)

    return data["Templates"]

def delete_template(name):

    # Delete reference in config.json
    with open("config.json", 'r') as f:
        data = json.load(f)
    
    for i in data["Templates"]:
        if i[0] == name:
            data["Templates"].remove(i)
    
    with open("config.json", 'w') as f:
        json.dump(data, f)

    # Delete txt file
    path = templates_path()
    file = f"{path}/{name}.txt"
    os.remove(file)


def create_template(name):
    window.extend_layout(window['new_column'], wd.template_button(template_name))

    template = Template(name)
    template.create_txt()
    

# scan for templates


 

window = wd.main(load_templates())
populated = False

while True:
    event, values = window.read()
    

    if event == sg.WIN_CLOSED:
        break

    elif event == "add_template":
        template_name = wd.name_input()
        create_template(template_name)

        select_events.append(template_name)
        edit_events.append(template_name)

    for e in edit_events:
        if event == f"{e}_edit":
            path = f"{templates_path()}/{e}.txt"
            os.startfile(path)
        elif event == f"{e}_delete":
            delete_template(e)

    for e in select_events:
        if event == f"{e}_select":
            path = f"{templates_path()}/{e}.txt"
            file = open(path, 'r').read()
            pyperclip.copy(file)

    

window.close()

