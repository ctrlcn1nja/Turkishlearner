from pyexcel_ods3 import save_data
from pyexcel_ods3 import get_data
import random
import math
import os
os.chdir("aditional files") # Change the working directory to the parent directory


def perfect_word(word):
    list_of_words = word.split()
    word = ''
    for elem in list_of_words:
        word += elem + ' '
    word = word[:-1]
    if word == '':
        return ''

    while word[-1] == ' ':
        word = word[:-1]

    while word[0] == ' ':
        word = word[1:]

    word = word.replace('İ', 'i')
    return word.lower()

def show_levels(data):
    level = str(math.ceil(math.log2(int(data))) + 1)
    if level == '1':
        return 'I'
    if level == '2':
        return 'II'
    if level == '3':
        return 'III'
    if level == '4':
        return 'IV'
    if level == '5':
        return 'V'
    if level == '6':
        return 'VI'
    if level == '7':
        return 'VII'
    if level == '8':
        return 'VIII'
    if level == '9':
        return 'IX'
    if level == '10':
        return 'X'


def adjust_data(random_word, direction, mode):
    #mode 1 - Spelling, 2 - Rus-Turk, 3 - Turk-Rus
    if mode == 1:
        column = 4
    elif mode == 2:
        column = 3
    else:
        column = 2
    # Even though here we can avoid if statements, I decided to keep them for the sake of clarity
    data = get_data("tk_words.ods")
    index = 1
    for data_slice in data['Sheet1'][1:]:
        if data_slice[0] == random_word:
            if direction == 'up':
                buff = settings_get('BUFFS')[mode - 1]
                data['Sheet1'][index][column] = min(2 ** (settings_get('MAX_LEVELS')[mode - 1] - 1), data['Sheet1'][index][column] * buff)
            else:
                debuff = settings_get('DEBUFFS')[mode - 1]
                data['Sheet1'][index][column] = max(1, data['Sheet1'][index][column] // debuff)
            break
        index += 1
    save_data("tk_words.ods", data)


def make_word_max_level(word, mode):
    if mode == 1:
        column = 4
    elif mode == 2:
        column = 3
    else:
        column = 2
    data = get_data("tk_words.ods")
    index = 1
    for data_slice in data['Sheet1'][1:]:
        if data_slice[0] == word:
            data['Sheet1'][index][column] = 2 ** (settings_get('MAX_LEVELS')[mode - 1] - 1)
            break
        index += 1
    save_data("tk_words.ods", data)


def reset_levels(MAX_LEVELS):
    data = get_data("tk_words.ods")
    for data_slice in data['Sheet1'][1:]:
        data_slice[2] = min(2 ** (MAX_LEVELS[2] - 1), data_slice[2]) # Turk-Rus
        data_slice[3] = min(2 ** (MAX_LEVELS[1] - 1), data_slice[3]) # Rus-Turk
        data_slice[4] = min(2 ** (MAX_LEVELS[0] - 1), data_slice[4]) # spelling
    save_data("tk_words.ods", data)


def random_word(mode):
    column = 5 - mode
    max_weight = 2 ** (settings_get('MAX_LEVELS')[mode - 1] + settings_get('MAX_LEVELS_WORDS')[mode - 1] - 2)
    data = get_data("tk_words.ods")
    weights = [max_weight // int(x[column]) for x in data['Sheet1'][1:]]
    random_word = random.choices(data['Sheet1'][1:], weights=weights)[0]
    return random_word


def levels_list():
    data = get_data("tk_words.ods")
    data_list = []
    for data_slice in data['Sheet1'][1:]:
        data_list.append([data_slice[4], data_slice[3], data_slice[2], data_slice[0], data_slice[1]])

    data_list.sort()
    str_list = ['Turkish' + " " * 18 + '|' + 'Russian' + " " * 18 + 'Levels: |Spelling|Rus-Turk|Turk-Rus|']
    for data_slice in data_list:
        str_list.append(f'{data_slice[3]:<25}|{data_slice[4]:<33}|{show_levels(data_slice[0]):>8}|{show_levels(data_slice[1]):>8}|{show_levels(data_slice[2]):>8}|')
    return str_list


def give_random_options(answer, mode):
    data = get_data("tk_words.ods")
    options = []
    val = 1
    while len(options) < 3:
        for data_slice in data['Sheet1'][1:]:
            if mode == 1:
                if data_slice[2] == val and data_slice[1] != answer:
                    options.append(data_slice[1])
            else:
                if data_slice[3] == val and data_slice[0] != answer:
                    options.append(data_slice[0])
        val *= 2
    random.shuffle(options)
    options = options[:3]
    options.append(answer)
    random.shuffle(options)
    if options[0] == answer:
        return options + ['A']
    elif options[1] == answer:
        return options + ['B']
    elif options[2] == answer:
        return options + ['C']
    return options + ['D']



def settings_get(key):
    stream = open("settings.txt", "r")
    settings = {}
    for line in stream:
        line = line.split()
        settings[line[0]] = [int(line[1]), int(line[2]), int(line[3])]
    stream.close()
    return settings[key]

def settings_set(key, value):
    stream = open("settings.txt", "r")
    settings = {}
    for line in stream:
        line = line.split()
        settings[line[0]] = [line[1], line[2], line[3]]
    stream.close()
    settings[key] = value
    stream = open("settings.txt", "w")
    for key in settings:
        stream.write(f'{key} {settings[key][0]} {settings[key][1]} {settings[key][2]}\n')
    stream.close()

