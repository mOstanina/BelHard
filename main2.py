# Написать функцию count_char, которая принимает строковое значение STR_VAL из которого создает и возвращает словарь

def count_char(STR_VAL):
    new_list = {}
    for element in STR_VAL:
        if new_list.get(element):
            new_list[element] += 1
        else:
            new_list[element] = 1
    return new_list


print(count_char("qwweeeertyyuuur"))
