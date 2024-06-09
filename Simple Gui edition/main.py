import PySimpleGUI as gui
import  functions
from playsound import playsound

def main_window():
    layout = [
        [gui.Text("Welcome to the main screen, please select an option")],
        [gui.Button("Turkish spelling"), gui.Button("Turkish to Russian (options)")],
        [gui.Button("Russian to Turkish (options)"), gui.Button("Levels")],
        ]
    window = gui.Window("Main", layout)
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED:
            break
        if event == "Turkish spelling":
            window.close()
            turkish_spelling()

        if event == "Turkish to Russian (options)":
            pass
        if event == "Russian to Turkish (options)":
            pass
        if event == "Levels":
            pass

def turkish_spelling():
    word = functions.random_word(3)
    layout = [
        [gui.Text("Welcome to the Turkish spelling screen, please select an option")],
        [gui.Text(word[1]), gui.InputText(enable_events=True)],
        [gui.Button("Enter"), gui.Button("Back")],
        ]
    window = gui.Window("Turkish Spelling", layout, return_keyboard_events=True)
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED:
            break
        if event == "Back":
            window.close()
            main_window()
            break
        if event == "Enter" or event == "\r":
            print(values[0])
            if functions.perfect_word(values[0]) == functions.perfect_word(word[0]):
                gui.popup("Correct!")
                playsound("Simple Gui edition/correct_sound.mp3")
                #functions.adjust_data(word[0], 'up', 4)



if __name__ == "__main__":
    main_window()

