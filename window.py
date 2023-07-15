import PySimpleGUI as sg
import json


WINDOW_NAME = "Email Template Tool"
font = ("Arial", 14)

def main(saved_templates):
    column_layout = []

    # displays saved templates
    for i in saved_templates:
        column_layout.append(template_button(i[0])[0])
        print(i[0])

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
            sg.Button("Edit Template", key=f"{name}_edit", font=font)
        ]
    ]

    return layout
    
    