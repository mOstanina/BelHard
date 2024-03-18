"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""
def yes_or_no(my_list):
    new_list = []
    for element in my_list:
        if element in new_list:
            print("Yes - ", element)
        else:
            print("No - ", element)
        new_list.append(element)


yes_or_no([3, 5, 6, 34, 6, 7])
