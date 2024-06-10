from pyexcel_ods3 import save_data
from pyexcel_ods3 import get_data
import random
import math
import os
os.chdir("..") # Change the working directory to the parent directory


def perfect_word(word):
    if word == '':
        return ''

    while word[-1] == ' ':
        word = word[:-1]

    while word[0] == ' ':
        word = word[1:]
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


def adjust_data(random_word, direction, column, buff=2):
    data = get_data("tk_words.ods")
    index = 1
    for data_slice in data['Sheet1'][1:]:
        if data_slice[0] == random_word:
            if direction == 'up':
                data['Sheet1'][index][column] = min(1024, data['Sheet1'][index][column] * buff)
            else:
                data['Sheet1'][index][column] = max(1, data['Sheet1'][index][column] // buff)
            break
        index += 1
    save_data("tk_words.ods", data)


def random_word(mode):
    data = get_data("tk_words.ods")
    weights = [8 // int(x[mode + 1]) for x in data['Sheet1'][1:]]
    random_word = random.choices(data['Sheet1'][1:], weights=weights)[0]
    return random_word


def levels_list(column):
    data = get_data("tk_words.ods")
    data_list = []
    for data_slice in data['Sheet1'][1:]:
        data_list.append([data_slice[int(column) + 1], data_slice[0], data_slice[1]])

    data_list.sort()
    str_list = ['Turkish' + " " * 18 + '|' + 'Russian' + " " * 18 + '|' + 'Level' + " " * 20]
    for data_slice in data_list:
        str_ = data_slice[1] + " " * (25 - len(data_slice[1])) + '|' + data_slice[2] + " " * (25 - len(data_slice[2])) + '|' + show_levels(data_slice[0]) + " " * (25 - len(show_levels(data_slice[0])))
        str_list.append(str_)
    return str_list