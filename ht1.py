"""
Создать класс BookCard,в классе должныбыть:
- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year.
В сеттерах сделать проверку на тип данных, если тип данных не подходит, то бросить ValueError.
Для года издания дополнительно проверить на валидность (> 0, <= текущего года).
Аксессоры реализоваться через property.
"""

from datetime import datetime


class BookCard:
    _author: str
    _title: str
    _year: int

    def __init__(self, author, title, year):
        self._author = author
        self._title = title
        self._year = year

    def __ge__(self, other):
        return self._year >= other._year

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        try:
            if type(value) is str:
                self._author = value
        except ValueError:
            print("неверное значение")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        try:
            if type(value) is str:
                self._title = value
        except ValueError:
            print("неверное значение")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        try:
            if type(value) is int and 0 < value <= datetime.now().year:
                self._year = value
        except ValueError:
            print("неверное значение")


a = BookCard("aaa", "aaaa", 1999)
b = BookCard("bbb", "bbbb", 2015)

print(a.__ge__(b))
print(b.__ge__(a))

a.year = 2026
print(a.year)
