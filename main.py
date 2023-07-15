import PySimpleGUI as sg
import json
import window as wd

class Template:
    def __init__(self, name):
        self.name = name
    

    def create_txt(self):
        pass
        # create path and variable for path

    pass



window = wd.main()

# scan for templates



while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == "add_template":
        template_name = wd.name_input()
        print(window)
        window.extend_layout(window['new_column'], wd.template_button(template_name))




window.close()

