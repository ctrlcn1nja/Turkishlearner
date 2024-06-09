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


