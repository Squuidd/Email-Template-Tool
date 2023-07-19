import PySimpleGUI as sg
import json
import window as wd
import os
import pyperclip



template_events = []
config_file = "config.json"

if '_MEIPASS2' in os.environ:
    config_file = os.path.join(os.environ['_MEIPASS2'], config_file)

def templates_path():
    absolute_path = os.path.dirname(__file__)
    relative_path = "Templates/"
    full_path = os.path.join(absolute_path, relative_path)

    if '_MEIPASS2' in os.environ:
        full_path = os.path.join(os.environ['_MEIPASS2'], full_path)
    # return full_path
    return "Templates\\"

class Template:
    def __init__(self, name):
        self.name = name
    
    def create_txt(self):
        path = templates_path()
        file = f"{path}/{self.name}.txt"
        
        if '_MEIPASS2' in os.environ:
            file = os.path.join(os.environ['_MEIPASS2'], file)

        open(file, "x")

        self.path = file
        self.save()

    def save(self):
        with open(config_file, 'r') as f:
            data = json.load(f)
        data["Templates"].append([self.name, self.path])

        with open(config_file, "w") as f:
            json.dump(data, f)

def name_checker(name):
    # Checks if name is empty
    if name == "":
        wd.error_message("The template must be named.")
        return False
    
    # Checks if name is already being used.
    with open(config_file, 'r') as f:
        data = json.load(f)
    
    for i in data["Templates"]:
        if i[0] == name:
            wd.error_message("This name is already used.")
            return False
        
    return True

def load_templates():
    with open(config_file, 'r') as f:
        data = json.load(f)

    for i in data["Templates"]:
        template_events.append(i[0])  
        

    return data["Templates"]

def delete_template(name):
    
    # Delete reference in config.json

    with open(config_file, 'r') as f:
        data = json.load(f)
    
    for i in data["Templates"]:
        if i[0] == name:
            data["Templates"].remove(i)
    
    with open(config_file, 'w') as f:
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

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == "add_template":
        template_name = wd.name_input()
        # name checker
        if name_checker(template_name):
            create_template(template_name)
            template_events.append(template_name)
            window.close()
            window = wd.main(load_templates())

    for e in template_events:
        if event == f"{e}_edit":
            path = f"{templates_path()}/{e}.txt"
            os.startfile(path)
            event = None
            
        
        elif event == f"{e}_select":
            path = f"{templates_path()}/{e}.txt"
            file = open(path, 'r').read()
            pyperclip.copy(file)
            event = None

        elif event == f"{e}_delete":
            if wd.confirm_delete(e): 
                try:
                    delete_template(e)
                except:
                    pass
                window.close()
                window = wd.main(load_templates())
            event = None
                

window.close()

