firstname = 'Maryia'
lastname = 'Ostanina'
age = '35'
print("Привет, меня зовут " + firstname + " " + lastname + ", мне " + age + " лет")
str1 = "Привет, меня зовут {} {}, мне {} лет".format(firstname, lastname, age)
print(str1)
str2 = f"Привет, меня зовут {firstname} {lastname}, мне {age} лет"
print(str2)

input_value = input('text something: ')
third_character = input_value[2]
print(third_character)
penultimate_character = input_value[-2]
print(penultimate_character)
line_slice = input_value[:5]
print(line_slice)
line_slice2 = input_value[:-3]
print(line_slice2)
some_str = 'Hello, world!'
new_str = some_str.replace('world', firstname)
print(new_str)