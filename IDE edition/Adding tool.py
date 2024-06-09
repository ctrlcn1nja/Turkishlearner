from pyexcel_ods3 import save_data
from pyexcel_ods3 import get_data
import os
os.chdir("..")

data = get_data("tk_words.ods")
stream = open("words_to_add.txt", "r", encoding="utf-8")
print('Are you sure you want to add these words?')
print('Y/N')
status = input()
if status != 'Y':
    exit(0)
for line in stream:
    #print([line.split('—')[0][:-1], line.split('—')[1][1:-1], 0, 0])
    data['Sheet1'].append([line.split('—')[0][:-1], line.split('—')[1][1:-1], 1, 1])

save_data("tk_words.ods", data)
print('Words added successfully!')