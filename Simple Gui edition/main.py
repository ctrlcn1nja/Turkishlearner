import PySimpleGUI as gui
import pygame
import  functions


pygame.init()
pygame.mixer.init()


def main_window():
    gui.theme('DarkAmber')  # You can choose a different theme if you like

    layout = [
        [gui.Text("Welcome to the main screen", font=("Helvetica", 32), justification='center', size=(30, 1))],
        [gui.Text("Please select an option", font=("Helvetica", 24), justification='center', size=(30, 1))],
        [gui.Button("Turkish spelling", font=("Helvetica", 16), size=(20, 2)), gui.Button("Turkish to Russian (options)",font=("Helvetica", 16), size=(20, 2))],
        [gui.Button("Russian to Turkish (options)",font=("Helvetica", 16), size=(20, 2)), gui.Button("Levels", font=("Helvetica", 16), size=(20, 2))]

    ]
    window = gui.Window("Main", layout, element_justification='center', finalize=True)
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED:
            break
        if event == "Turkish spelling":
            window.close()
            turkish_spelling()

        if event == "Turkish to Russian (options)":
            window.close()
            tk_to_ru_options()
        if event == "Russian to Turkish (options)":
            window.close()
            ru_to_tk_options()
        if event == "Levels":
            window.close()
            levels_window()

def turkish_spelling():
    word = functions.random_word(3)
    layout = [
        [gui.Text("Welcome to the Turkish spelling screen", font=("Helvetica", 16), justification='center',
                 size=(40, 1))],
        [gui.Text("Please spell the following word:", font=("Helvetica", 16), justification='center', size=(40, 1))],
        [gui.Text(word[1], font=("Helvetica", 18), background_color='black', justification='center', size=(28, 1))],
        [gui.InputText(enable_events=True, focus=True, font=("Helvetica", 18), justification='center', size=(30, 1))],
        [gui.Button("BACK", size=(23, 2)), gui.Button("ENTER", size=(23, 2))]
    ]

    window = gui.Window("Turkish Spelling", layout, element_justification='center', return_keyboard_events=True,
                       finalize=True)
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED:
            break
        if event == "BACK":
            window.close()
            main_window()
            break
        if event == "ENTER" or event == "\r":
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
                show_incorrect_answer_popup(word[0])
                functions.adjust_data(word[0], 'down', 4)
                window.close()
                turkish_spelling()


def levels_window():
    levels = functions.levels_list(3)
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


def tk_to_ru_options():
    word = functions.random_word(1)
    options = functions.give_random_options(word[1], 1)
    layout = [
        [gui.Text("Turkish to Russian Options", font=("Helvetica", 16), justification='center', size=(40, 1))],
        [gui.Text('Please select the translation of the following word:', font=("Helvetica", 14), justification='center', size=(40, 1))],
        [gui.Text(word[0], font=("Helvetica", 18), background_color='black', justification='center', size=(30, 1))],
        [gui.Button(options[0], size=(25, 2)), gui.Button(options[1], size=(25, 2))],
        [gui.Button(options[2], size=(25, 2)), gui.Button(options[3], size=(25, 2))]
    ]

    window = gui.Window("Turkish to Russian Options", layout, element_justification='center',
                       return_keyboard_events=True, finalize=True)
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED:
            main_window()
            break
        if (event == word[1]
                or (event == '1' and options[4] == 'A')
                or (event == '2' and options[4] == 'B')
                or (event == '3' and options[4] == 'C')
                or (event == '4' and options[4] == 'D')):
            pygame.mixer.music.load('correct_sound_1.wav')
            pygame.mixer.music.play()
            window.close()
            functions.adjust_data(word[0], 'up', 2)
            tk_to_ru_options()
        elif ((event == options[0])
              or (event == options[1])
              or (event == options[2])
              or (event == options[3])
                or (event == '1')
                or (event == '2')
                or (event == '3')
                or (event == '4')):
            pygame.mixer.music.load('wrong_answer_1.wav')
            pygame.mixer.music.play()
            show_incorrect_answer_popup(word[1])
            window.close()
            functions.adjust_data(word[0], 'down', 2)
            tk_to_ru_options()


def ru_to_tk_options():
    word = functions.random_word(2)
    options = functions.give_random_options(word[0], 2)
    layout = [
        [gui.Text("Turkish to Russian Options", font=("Helvetica", 16), justification='center', size=(40, 1))],
        [gui.Text('Please select the translation of the following word:', font=("Helvetica", 14),
                  justification='center', size=(40, 1))],
        [gui.Text(word[1], font=("Helvetica", 18), background_color='black', justification='center', size=(30, 1))],
        [gui.Button(options[0], size=(25, 2)), gui.Button(options[1], size=(25, 2))],
        [gui.Button(options[2], size=(25, 2)), gui.Button(options[3], size=(25, 2))]
    ]
    window = gui.Window("Russian to Turkish options", layout, return_keyboard_events=True, element_justification='center', finalize=True)
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED:
            window.close()
            main_window()
            break
        if (event == word[0]
                or (event == '1' and options[4] == 'A')
                or (event == '2' and options[4] == 'B')
                or (event == '3' and options[4] == 'C')
                or (event == '4' and options[4] == 'D')):
            pygame.mixer.music.load('correct_sound_1.wav')
            pygame.mixer.music.play()
            window.close()
            functions.adjust_data(word[0], 'up', 3)
            ru_to_tk_options()
        elif ((event == options[0])
              or (event == options[1])
              or (event == options[2])
              or (event == options[3])
                or (event == '1')
                or (event == '2')
                or (event == '3')
                or (event == '4')):
            pygame.mixer.music.load('wrong_answer_1.wav')
            pygame.mixer.music.play()
            show_incorrect_answer_popup(word[0])
            window.close()
            functions.adjust_data(word[0], 'down', 3)
            ru_to_tk_options()


def show_incorrect_answer_popup(correct_word):  # Ensure consistent theme across the application

    layout = [
        [gui.Text("Incorrect Answer", font=("Helvetica", 16), justification='center')],
        [gui.Text(f"The correct answer is:", font=("Helvetica", 14), justification='center')],
        [gui.Text(correct_word, font=("Helvetica", 18), background_color='black', justification='center')],
        [gui.Button("OK", size=(10, 1))]
    ]

    window = gui.Window("Incorrect Answer", layout, element_justification='center', modal=True, finalize=True)

    while True:
        event, values = window.read()
        if event == gui.WINDOW_CLOSED or event == "OK":
            break

    window.close()










if __name__ == "__main__":
    main_window()

