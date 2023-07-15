import PySimpleGUI as sg

WINDOW_NAME = "Email Template Tool"
font = ("Arial", 14)

def main():
    column_layout = []

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
    return [[sg.Button(name, key=f"{name}_select", font=font)]]
    