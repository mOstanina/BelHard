class Dog:
    """ Класс Dog.
        Имеет имеет атрибуты: height, weight, name, age.
        Класс имеет методы: jump, run, bark, change_nam который  принимает на вход новое имя и меняет атрибут имени у объекта
    """
    height: int
    weight: int
    name: str
    age: int

    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age


    def jump(self):
        print("jump")

    def run(self):
        print("run")

    def bark(self):
        print("bark")

    def change_name(self, new_name):
        self.name = new_name


dog = Dog(20, 5, "Nik", 4)

print("старое имя", dog.name)

dog.change_name("Tommy")

print("новое имя", dog.name)