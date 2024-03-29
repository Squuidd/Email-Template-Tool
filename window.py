import PySimpleGUI as sg
import json



WINDOW_NAME = "Email Template Tool"
font = ("Arial", 12)

def sort_templates(names):
    name_list = []
    for name in names:
        name_list.append(name[0])

    try: 
        name_list.sort(key=lambda v: v.upper())
        # This breaks if there is a None object
    except:
        pass

    return name_list

def main(saved_templates):
    main_column = [] #Alphabetize this list
    edit_column = []

    sorted_names = sort_templates(saved_templates)
    # displays saved templates
    for i in sorted_names: #saved_templates
        #main_column.append(template_button(i[0])[0])
        main_column.append(template_button(i)[0])
        edit_column.append(edit_layout(i)[0])

    

    layout = [
        [
            sg.Button("Add Template", key="add_template", font=font)
        ],
        [
            sg.Column(main_column, key="new_column"),
            sg.Column(edit_column, key="edit_column")
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
            name = name_field[0][0].get()

            return name

        if event == sg.WIN_CLOSED:
            break

    window.close()

def template_button(name):
    layout = [
        [
            sg.Button(name, key=f"{name}_select", font=font),
            # sg.Button("Edit Template", key=f"{name}_edit", font=font),
            # sg.Button("Delete Template", key=f"{name}_delete", font=font)
        ]
    ]

    return layout

def edit_layout(name):
    layout = [
        [
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

    
    window = sg.Window("Caution", layout)

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
        
def error_message(message):
    layout = [
        [
            sg.Text(message, font=font)
        ],
        [
            sg.Button("Ok", key="error_acknowledge", font=font)
        ]
    ]

    window = sg.Window("Warning", layout=layout)

    while True:
        event, values = window.read()

        if event == "error_acknowledge":
            break

        elif event == sg.WIN_CLOSED:
            break

    window.close()

