import PySimpleGUI as gui
import pygame
import  functions
import uuid # for generating unique file names


pygame.init()
pygame.mixer.init()


def main_window():
    gui.theme('DarkAmber')  # You can choose a different theme if you like

    layout = [
        [gui.Text("Welcome to the main screen", font=("Helvetica", 32), justification='center', size=(30, 1))],
        [gui.Text("Please select an option:", font=("Helvetica", 24), size=(23, 1), justification='center'), gui.Button(image_filename='gear.png', image_size=(50, 50), key='settings')],
        [gui.Button("Turkish spelling", font=("Helvetica", 16), size=(20, 2)), gui.Button("Turkish to Russian (options)",font=("Helvetica", 16), size=(20, 2))],
        [gui.Button("Russian to Turkish (options)",font=("Helvetica", 16), size=(20, 2)), gui.Button("Levels", font=("Helvetica", 16), size=(20, 2))],

    ]
    window = gui.Window("Main", layout, element_justification='center', finalize=True)
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED:
            window.close()
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
        if event == 'settings':
            window.close()
            settings_window()

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
            if functions.perfect_word(values[0]) == functions.perfect_word(word[0]):
                pygame.mixer.music.load('correct_sound_1.wav')
                pygame.mixer.music.play()
                functions.adjust_data(word[0], 'up', 4)
                window.close()
                turkish_spelling()
                break
            else:
                pygame.mixer.music.load('wrong_answer_1.wav')
                pygame.mixer.music.play()
                show_incorrect_answer_popup(word[0])
                functions.adjust_data(word[0], 'down', 4)
                window.close()
                turkish_spelling()
                break


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
            window.close()
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
            break
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
            break


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
            break
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
            break

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


def settings_window():
    global MAX_LEVELS, MAX_LEVELS_WORDS, BUFFS, DEBUFFS # Ensure that the global variables are accessible

    note = ("NOTE: If you reach the maximum level for all words, the program will revisit all the words, "
             "to identify any that may have become weak. "
             "After this review, the program will return to its normal mode of operation.")

    tab1_layout = [
        [gui.Text('Select max level for a word:', font=("Helvetica", 16), size=(30, 1))],
        [gui.Slider(range=(1, 10), default_value=MAX_LEVELS[0], orientation='h', size=(30, 15), key='-SLIDER11-',
                    font=("Helvetica", 14))],
        [gui.Text('Set the buff and debuff for the correct and incorrect answers accordingly:',
                  font=("Helvetica", 16))],
        [gui.Slider(range=(0, 3), default_value=BUFFS[0], orientation='h', size=(30, 15), key='-SLIDER12-',
                    font=("Helvetica", 14)),
         gui.Slider(range=(-3, 0), default_value=DEBUFFS[0], orientation='h', size=(30, 15), key='-SLIDER13-',
                    font=("Helvetica", 14))],
        [gui.Text('Should max-level words be still in the pool?', font=("Helvetica", 16))],
        [gui.Radio('Yes', default=MAX_LEVELS_WORDS[0], group_id=11, key='-YES-', font=("Helvetica", 14)),
         gui.Radio('No', default=(1 - MAX_LEVELS_WORDS[0]), group_id=11, key='-NO-', font=("Helvetica", 14))],
        [gui.Multiline(note, size=(600, 3), font=("Helvetica", 16), no_scrollbar=True)],
    ]

    tab2_layout = [
        [gui.Text('Select max level for a word:', font=("Helvetica", 16), size=(30, 1))],
        [gui.Slider(range=(1, 10), default_value=MAX_LEVELS[1], orientation='h', size=(30, 15), key='-SLIDER21-',
                    font=("Helvetica", 14))],
        [gui.Text('Set the buff and debuff for the correct and incorrect answers accordingly:',
                  font=("Helvetica", 16))],
        [gui.Slider(range=(0, 3), default_value=BUFFS[1], orientation='h', size=(30, 15), key='-SLIDER22-',
                    font=("Helvetica", 14)),
         gui.Slider(range=(-3, 0), default_value=DEBUFFS[1], orientation='h', size=(30, 15), key='-SLIDER23-',
                    font=("Helvetica", 14))],
        [gui.Text('Should max-level words be still in the pool?', font=("Helvetica", 16))],
        [gui.Radio('Yes', default=MAX_LEVELS_WORDS[1], group_id=21, key='-YES-', font=("Helvetica", 14)),
         gui.Radio('No', default=(1 - MAX_LEVELS_WORDS[1]), group_id=21, key='-NO-', font=("Helvetica", 14))],
        [gui.Multiline(note, size=(600, 3), font=("Helvetica", 16), no_scrollbar=True)],

    ]
    tab3_layout = [
        [gui.Text('Select max level for a word:', font=("Helvetica", 16), size=(30, 1))],
        [gui.Slider(range=(1, 10), default_value=MAX_LEVELS[2], orientation='h', size=(30, 15), key='-SLIDER31-', font=("Helvetica", 14))],
        [gui.Text('Set the buff and debuff for the correct and incorrect answers accordingly:', font=("Helvetica", 16))],
        [gui.Slider(range=(0, 3), default_value=BUFFS[2], orientation='h', size=(30, 15), key='-SLIDER32-', font=("Helvetica", 14)), gui.Slider(range=(-3, 0), default_value=DEBUFFS[2], orientation='h', size=(30, 15), key='-SLIDER33-', font=("Helvetica", 14))],
        [gui.Text('Should max-level words be still in the pool?', font=("Helvetica", 16))],
        [gui.Radio('Yes', default=MAX_LEVELS_WORDS[2], group_id=31, key='-YES-', font=("Helvetica", 14)), gui.Radio('No', default=(1 - MAX_LEVELS_WORDS[2]), group_id=31, key='-NO-', font=("Helvetica", 14))],
        [gui.Multiline(note, size=(600, 3), font=("Helvetica", 16), no_scrollbar=True)],
    ]

    settings_layout = [
        [gui.TabGroup([[gui.Tab('Turkish Spelling',  tab1_layout, font=("Helvetica", 32)), gui.Tab('Turkish to Russian (options)', tab2_layout, font=("Helvetica", 32)), gui.Tab('Russian to Turkish (options)', tab3_layout, font=("Helvetica", 32))]], size=(800, 600))],
        [gui.Button("Save"), gui.Button("Cancel"), gui.Button("Reset to Default")]
    ]

    settings_window = gui.Window("Settings", settings_layout, finalize=True)
    while True:
        event, values = settings_window.read()
        if event == gui.WIN_CLOSED or event == "Cancel":
            settings_window.close()
            main_window()
            break
        if event == "Save":
            MAX_LEVELS = [int(values['-SLIDER11-']), int(values['-SLIDER21-']), int(values['-SLIDER31-'])]
            BUFFS = [int(values['-SLIDER12-']), int(values['-SLIDER22-']), int(values['-SLIDER32-'])]
            DEBUFFS = [int(values['-SLIDER13-']), int(values['-SLIDER23-']), int(values['-SLIDER33-'])]
            MAX_LEVELS_WORDS = [values['-YES-'], values['-YES-'], values['-YES-']]
            settings_window.close()
            main_window()
            break
        if event == "Reset to Default":
            MAX_LEVELS = [5, 10, 10]
            BUFFS = [1, 1, 1]
            DEBUFFS = [-1, -1, -1]
            MAX_LEVELS_WORDS = [True, True, True]
            settings_window.close()
            settings_window()







if __name__ == "__main__":
    MAX_LEVELS = [5, 10, 10]
    BUFFS = [1, 1, 1]
    DEBUFFS = [-1, -1, -1]
    MAX_LEVELS_WORDS = [False, True, True]
    # Ensure that the global variables are accessible
    main_window()

