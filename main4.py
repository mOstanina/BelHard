# С помощью декораторов реализовать конвейер сборки бургера

def bread(func):
    def wrapper():
        print("<//----------\\>")
        func()
        print("<\\----------//>")
    return wrapper


def tomato(func):
    def wrapper():
        print("****помидоры****")
        func()
    return wrapper


def salad(func):
    def wrapper():
        print("~~~~~салат~~~~~")
        func()
    return wrapper


def cheese(func):
    def wrapper():
        print("^^^^^сыр^^^^^")
        func()
    return wrapper


def onion(func):
    def wrapper():
        print("-----лук-----")
        func()
    return wrapper


"""
Собрать с помощью декораторов гамбургер:
булка
лук
помидоры
говядина
булка
"""


@bread
@onion
@tomato
def beef():
    print("###говядина###")


"""
Собрать с помощью декораторов гамбургер:
булка
сыр
курица
булка
"""


@bread
@cheese
@salad
def chicken():
    print("|||курица|||")


beef()
chicken()
