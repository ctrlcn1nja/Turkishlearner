import PySimpleGUI as gui

def main_window():
    layout = [
        [gui.Text("Welcome to the main screen, please select an option")],
        [gui.Button("Turkish spelling"), gui.Button("Turkish to Russian (options)")],
        [gui.Button("Russian to Turkish (options)"), gui.Button("Levels")],
        ]
    return gui.Window("Main Screen", layout)

def turkish_spelling():
    layout = [
        [gui.Text("Welcome to the Turkish spelling screen, please select an option")],
        [gui.Text("Word: "), gui.InputText()],
        [gui.Button("Start"), gui.Button("Back")],
        ]
    return gui.Window("Turkish Spelling", layout)



window = main_window()
while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED:
        break
    if event == "Turkish spelling":
        window.close()
        window = turkish_spelling()
    if event == "Turkish to Russian (options)":
        pass
    if event == "Russian to Turkish (options)":
        pass
    if event == "Levels":
        pass