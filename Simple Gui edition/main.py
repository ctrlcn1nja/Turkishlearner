import PySimpleGUI as gui
import pygame
import  functions


pygame.init()
pygame.mixer.init()


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
            window.close()
            levels_window()

def turkish_spelling():
    word = functions.random_word(3)
    layout = [
        [gui.Text("Welcome to the Turkish spelling screen, please select an option")],
        [gui.Text(word[1]), gui.InputText(enable_events=True, focus=True)],
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
                pygame.mixer.music.load('correct_sound_1.wav')
                pygame.mixer.music.play()
                functions.adjust_data(word[0], 'up', 4)
                window.close()
                turkish_spelling()
            else:
                pygame.mixer.music.load('wrong_answer_1.wav')
                pygame.mixer.music.play()
                gui.popup("Incorrect, the correct answer is: " + word[0])
                functions.adjust_data(word[0], 'down', 4)
                window.close()
                turkish_spelling()


def levels_window():
    levels = functions.levels_list(3)
    print(levels[0])
    print(levels[1])
    print(levels[2])
    layout = [[gui.Listbox(values=levels, size=(100, 30), font=('courier', 12))],
              [gui.Button("Back")],
              ]
    window = gui.Window("Levels", layout)
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED:
            break
        if event == "Back":
            window.close()
            main_window()
            break












if __name__ == "__main__":
    main_window()

