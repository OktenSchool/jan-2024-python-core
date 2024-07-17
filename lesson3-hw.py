# # Створити клас Rectangle:
# # -він має приймати дві сторони x,y
# # -описати поведінку на арифметични методи:
# #   + сумма площин двох екземплярів ксласу
# #   - різниця площин двох екземплярів ксласу
# #   == площин на рівність
# #   != площин на не рівність
# #   >, < меньше більше
# #   при виклику метода len() підраховувати сумму сторін
# #
# #   ###############################################################################
# from typing import Self
#
#
# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.area = self.a * self.b
#
#     def __add__(self, other: Self):
#         return self.area + other.area
#
#     def __sub__(self, other: Self):
#         return self.area - other.area
#
#     def equals(self, other: Self):
#         return self.area == other.area
#
#     def __ne__(self, other: Self):
#         return self.area != other.area
#
#     def __gt__(self, other: Self):
#         return self.area > other.area
#
#     def lt__(self, other: Self):
#         return self.area < other.area
#
#     def __len__(self):
#         return (self.a + self.b) * 2
#
#
# # створити класс Human (name, age)
# # створити два класси Prince и Cinderella які наслідуються від Human:
# # у попелюшки мае бути ім'я, вік, розмір нонги
# # у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
# #
# # в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# # також має бути метод классу який буде виводити це значення
# #
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Cinderella(Human):
#     __count = 0
#
#     def __init__(self, name, age, size):
#         super().__init__(name, age)
#         self.size = size
#         Cinderella.__count += 1
#     def __str__(self):
#         return str(self.__dict__)
#     @classmethod
#     def show_counts(cls):
#         print(cls.__count)
#
#
# class Prince(Human):
#     def __init__(self, name, age, foot_size):
#         super().__init__(name, age)
#         self.foot_size = foot_size
#
#     def find_cinderella(self, cinderellas: list[Cinderella]):
#         for cinderella in cinderellas:
#             if cinderella.size == self.foot_size:
#                 print(cinderella)
#                 return
#         print('Not found!!!')
#
#
# cind: list[Cinderella] = [
#     Cinderella("Olha", 15, 30),
#     Cinderella("Kamila", 24, 32),
#     Cinderella("Albina", 18, 42),
#     Cinderella("Karina", 30, 36),
#     Cinderella("Julia", 12, 31),
# ]
#
# prince = Prince("Kokos", 2, 422)
# prince.find_cinderella(cind)
# Cinderella.show_counts()
# ###############################################################################
#
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# Приклад:
#
# Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))
#
#     Main.show_all_magazines()
#     print('-' * 40)
#     Main.show_all_books()

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):

    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'Book name: {self.name}')


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'Magazine name: {self.name}')


class Main:
    __printable_list: list[Printable] = []

    @classmethod
    def add(cls, item):
        if isinstance(item, (Magazine, Book)):
            cls.__printable_list.append(item)

    @classmethod
    def show_books(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()

    @classmethod
    def show_magazines(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()


Main.add(Book('book1'))
Main.add(Magazine('magazine2'))
Main.add(Book('book2'))
Main.add(Magazine('magazine1'))
Main.add(Magazine('magazine3'))
Main.add(Book('book3'))


Main.show_magazines()
print('*'*20)
Main.show_books()

