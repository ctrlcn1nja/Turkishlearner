from pyexcel_ods3 import save_data
from pyexcel_ods3 import get_data

name_of_input = input('Enter the name of the file you want to add: ')
data_to_add = get_data(name_of_input)
data = get_data("tk_words.ods")
#print(data_to_add)
for data_slice in data_to_add['Лист1'][1:]:
    if data_slice == []:
        continue
    data_slice += [1, 1, 1]
    print(data_slice[0], '-', data_slice[1])
    data['Sheet1'].append(data_slice)

decision = input('Are you sure you want to add these words? Y/N: ')
if decision == 'Y':
    save_data("tk_words.ods", data)
    print('Words added successfully!')
