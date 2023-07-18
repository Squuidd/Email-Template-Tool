import PySimpleGUI as sg
import json


WINDOW_NAME = "Email Template Tool"
font = ("Arial", 12)

def sort_templates(names):
    name_list = []
    for name in names:
        name_list.append(name[0])

    name_list.sort(key=lambda v: v.upper())

    return name_list

def main(saved_templates):
    column_layout = [] #Alphabetize this list

    sorted_names = sort_templates(saved_templates)
    # displays saved templates
    for i in sorted_names: #saved_templates
        #column_layout.append(template_button(i[0])[0])
        column_layout.append(template_button(i)[0])

    layout = [
        [
            sg.Button("Add Template", key="add_template", font=font)
        ],
        [
            sg.Column(column_layout, key="new_column") 
        ]
    ]

    return sg.Window(WINDOW_NAME, layout)

def name_input():
    name_field = [
        [
            sg.InputText(key="name", enable_events=True, size=(400, 90), font=font)
        ]
    ]

    layout = [
        [
            sg.Frame("Enter Template Name: ", layout=name_field, size=(500, 52), font=font),
            sg.Button("Submit", key="template_name", font=("Arial", 16))
        ]
    ]

    window = sg.Window(WINDOW_NAME, layout)

    while True:
        event, values = window.read()

        if event == "template_name":
            window.close()
            return name_field[0][0].get()

        if event == sg.WIN_CLOSED:
            break

    window.close()

def template_button(name):
    layout = [
        [
            sg.Button(name, key=f"{name}_select", font=font),
            sg.Button("Edit Template", key=f"{name}_edit", font=font),
            sg.Button("Delete Template", key=f"{name}_delete", font=font)
        ]
    ]

    return layout
    
def confirm_delete(name):
    layout = [
        [
            sg.Text(f"Are you sure want to delete [{name}]?", font=font)
        ],
        [
            sg.Button("Yes", key=f"destroy_{name}", font=font),
            sg.Button("No", key=f"destroy_cancel", font=font)
        ]
    ]

    
    window = sg.Window("", layout)

    while True:
        event, values = window.read()
        print(event)
        if event == f"destroy_{name}":
            window.close()
            return True

        elif event == "destroy_cancel":
            break
        
        elif event == sg.WIN_CLOSED:
            break

    window.close()
    return False
        
        
