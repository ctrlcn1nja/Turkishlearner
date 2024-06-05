from pyexcel_ods3 import save_data
from pyexcel_ods3 import get_data
import random
import math



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


def perfect_word(word):
    while word[-1] == ' ':
        word = word[:-1]

    while word[0] == ' ':
        word = word[1:]
    return word.lower()


def print_random_options(data, answer, mode):
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
    print("Option A:" + options[0])
    print("Option B:" + options[1])
    print("Option C:" + options[2])
    print("Option D:" + options[3])
    if options[0] == answer:
        return 'A'
    elif options[1] == answer:
        return 'B'
    elif options[2] == answer:
        return 'C'
    return 'D'


def adjust_data(data, random_word, direction, column, buff=2):
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



data = get_data("tk_words.ods")
print("What mode do you want to use?")
print("1.Turkish to Russian (options)")
print("2.Russian to Turkish (options)")
print("3.Turkish spelling")
print("s.To open data settings")
print('l. To show levels of the words')
mode = input('Enter the mode:')
if mode == '1':
    condition = True
    while condition:
        weights = [1024 // int(x[2]) for x in data['Sheet1'][1:]]
        random_word = random.choices(data['Sheet1'][1:], weights=weights)[0]
        print(random_word[0])
        actual_answer = print_random_options(data, random_word[1], 1)
        user_answer = input("Enter the answer: ")
        if perfect_word(user_answer) == perfect_word(actual_answer):
            print('--------------------------------------------------')
            print("Correct!")
            print('--------------------------------------------------')
            adjust_data(data, random_word[0], 'up', 2, 2)

        else:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print("Incorrect!, the correct answer is: " + actual_answer)
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            adjust_data(data, random_word[0], 'down', 2, 4)

if mode == '2':
    condition = True
    while condition:
        weights = [1024 // int(x[3]) for x in data['Sheet1'][1:]]
        random_word = random.choices(data['Sheet1'][1:], weights=weights)[0]
        print(random_word[1])
        actual_answer = print_random_options(data, random_word[0], 2)
        user_answer = input("Enter the answer: ")
        if perfect_word(user_answer) == perfect_word(actual_answer):
            print('--------------------------------------------------')
            print("Correct!")
            print('--------------------------------------------------')
            adjust_data(data, random_word[0], 'up', 3, 2)

        else:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print("Incorrect!, the correct answer is: " + actual_answer)
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            adjust_data(data, random_word[0], 'down', 3,4)

if mode == '3':
    condition = True
    while condition:
        weights = [32 // int(x[4]) for x in data['Sheet1'][1:]]
        random_word = random.choices(data['Sheet1'][1:], weights=weights)[0]
        print(random_word[1])
        user_answer = input("Enter the answer: ")
        if perfect_word(user_answer) == perfect_word(random_word[0]):
            print('--------------------------------------------------')
            print("Correct!")
            print('--------------------------------------------------')
            adjust_data(data, random_word[0], 'up', 4, 2)

        else:
            #print(user_answer, random_word[0].lower())
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print("Incorrect!, the correct answer is: " + random_word[0])
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            adjust_data(data, random_word[0], 'down', 4, 2)

if mode == 's':
    print("What do you want to do?")
    print("1.Reset all weights")
    print("2.Reset specific column")

    action = input('Enter the action:')
    if action == '1':
        for data_slice in data['Sheet1'][1:]:
            data_slice[2] = 1
            data_slice[3] = 1
            data_slice[4] = 1
        save_data("tk_words.ods", data)
        print('Weights reset successfully!')
    if action == '2':
        print("Which column do you want to reset?")
        print("1.Turkish to Russian")
        print("2.Russian to Turkish")
        print("3.Turkish spelling")
        column = input('Enter the column:')
        for data_slice in data['Sheet1'][1:]:
            data_slice[int(column) + 1] = 1
        save_data("tk_words.ods", data)
        print('Column reset successfully!')

if mode == 'l':
    print('In which column do you want to see the levels?')
    print('1.Turkish to Russian (options)')
    print('2.Russian to Turkish (options)')
    print('3.Turkish spelling')
    column = input('Enter the column:')
    data_list = []
    for data_slice in data['Sheet1'][1:]:
        data_list.append([data_slice[int(column) + 1], data_slice[0], data_slice[1]])

    data_list.sort()
    print('Turkish word              | Russian word                      | Level')
    for data_slice in data_list:
        print(f'{data_slice[1]:<25} | {data_slice[2]:<33} | {show_levels(data_slice[0])}')








