# 1.
# Создать два списка произвольного содержания:
first_list = [1, 2, 3, 4]
second_list = ["aaa", "bb", "ccc"]
print("первый список", first_list)
print("второй список", second_list)
# Добавить к каждому списку по одному элементу в конец и в начало
first_list.append(5)
first_list.insert(0, 0)
second_list.append("abcd")
second_list.insert(0, "00000")
print("первый список после добавления элементов в начало и конец", first_list)
print("второй список после добавления элементов в начало и конец", second_list)
# Расширить первый список вторым
first_list.extend(second_list)
print("первый список расширенный вторым", first_list)

# 2.
# Создать два списка с одинаковым кол-вом элементов. Сделать из этих списков словарь
list_1 = [1, 2, 3]
list_2 = ["a", "b", "c"]
new_dict = dict()
new_dict[list_1[0]] = list_2[0]
new_dict[list_1[1]] = list_2[1]
new_dict[list_1[2]] = list_2[2]
print("словарь из списков", new_dict)

# 3.
# Работа с Дзен Python
# ● Количество строк: Определите количество строк в Дзене Питона.
# ● Ключевые слова: Подсчитайте количество вхождений ключевых
#    слов из Дзена Питона, таких как "is", "and", "or". Сложить в
#   словарь такого типа {“is”: 4, “and”: None, “or”: 100}
# ● Замена слова: Замените все вхождения слова "is" в Дзене Питона
#   на "is not".


import this
zen = "".join([this.d.get(c, c) for c in this.s]) # как  еще вытащить zen и положить в переменную не нагуглила :(

count_of_strings = len(zen.split('\n'))
print("число строк в Zen", count_of_strings)

is_count = zen.count("is")
print("количество 'is'", is_count)
and_count = zen.count("and")
print("количество 'and'", and_count)
or_count = zen.count("or")
print("количество 'or'", or_count)
new_zen = zen.replace("is", "is not", is_count)
print("Zen с замененными 'is' на 'is not'", new_zen)
