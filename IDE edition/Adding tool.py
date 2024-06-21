from pyexcel_ods3 import save_data
from pyexcel_ods3 import get_data
import os
os.chdir("..")

data = get_data("tk_words.ods")
stream = open("IDE edition/words_to_add.txt", "r", encoding="utf-8")
print('Are you sure you want to add these words?')
print('Y/N')
status = input()
if status != 'Y':
    exit(0)

i = 0
word = []
for line in stream:
    if line[-1] == '\n':
        line = line[:-1]
    word.append(line)
    i += 1
    if i % 2 == 0:
        print(word)
        data['Sheet1'].append([word[0], word[1], 1, 1, 1])
        word = []

if word != []:
    print(word)
    data['Sheet1'].append([word[0], word[1], 1, 1, 1])
save_data("tk_words.ods", data)
print('Words added successfully!')