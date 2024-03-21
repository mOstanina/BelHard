class Dog:
    """ Класс Dog.
        Имеет имеет атрибуты: height, weight, name, age.
        Класс имеет методы: jump, run, bark.
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


dog = Dog(20, 5, "Nik", 4)

dog.jump()
dog.run()
dog.bark()


print(vars(dog))
print(dir(dog))

