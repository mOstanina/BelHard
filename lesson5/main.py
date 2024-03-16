# """1.
# В семье свадьба. Они решили выбрать заведение, где будут праздновать в зависимости от количества людей, которое прибудет к утру.
# Если их будет больше 50 - закажут ресторан
# если от 20 до 50 -то кафе,
# а если меньше 20 то отпраздную дома.
# Вывести "ресторан", "кафе", "дом" в зависимости от количества гостей"""
#
# count = int(input("Количество гостей: "))
# if count > 50:
#     print("ресторан")
# elif 50 >= count >= 20:
#     print("кафе")
# else:
#     print("дом")
#
# """2.
# Ввести строку. Если длина строки больше 10 символов, то создать новую строку с 3 восклицательными знаками в конце ('!!!')
# и вывести на экран. Если меньше 10, то вывести на экран второй символ строки"""
#
# input_string = input("Введите строку: ")
#
# if len(input_string) > 10:
#     print(f"{input_string}!!!")
# else:
#     try:
#         print(input_string[4])
#     except: print("недостаточно символов")

"""3.
Получить на ввод количество рублей и копеек и вывести в правильной форме, например, 3 рубля, 1 рубль 25 копеек, 3 копейки
● До10р*
● До100р**
● До 1000р ***"""

rub = None
cop = None
rub_string = ""
cop_string = ""

while rub is None:
    try:
        rub = int(input("Рублей: "))
        rubl = rub % 10
        if rubl == 1:
            rub_string = "рубль"
        elif rubl == 0 or rubl >= 5:
            rub_string = "рублей"
        else:
            rub_string = "рубля"
    except ValueError: print("неверное значение")

while cop is None:
    try:
        cop = int(input("Копеек: "))
        copi = cop % 10
        if cop >= 100:
            cop = None
            print("нельзя более 99 копеек")
        elif copi == 1:
            cop_string = "копейка"
        elif copi == 0 or copi >= 5:
            cop_string = "копеек"
        else:
            cop_string = "копейки"
    except ValueError:
        print("неверное значение")

print(f"{rub} {rub_string} и {cop} {cop_string}")
