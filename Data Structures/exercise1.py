# print the largest number in the list
number_list = [5, 7, 12, 9, -5, 10]
max_number = number_list[0]

for number in number_list:
    if number > max_number:
        max_number = number
print(max_number)