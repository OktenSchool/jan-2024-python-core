# CamelCase

# class User:
#     count = 0
#
#
# user1 = User()
# user2 = User()
#
# User.count = 55
# user1.count = 25
# print(user1.count)
# print(User.count)

# class User:
#     __slots__ = ('name', 'age', 'house')
#
#     def __init__(self, name, age, house):
#         self.name = name
#         self.age = age
#         self.house = house
#
#     def get_name(self):
#         return self.name
#
#     def __str__(self):
#         return f'{self.name} -- {self.age} -- {self.house}'
#
#     def __repr__(self):
#         return self.__str__()
#
#
# user_max = User("Max", 15, 25)
# user_kira = User("Kira", 20, 25)
# # print(user_kira.status)
# print(user_max.get_name())
#
# print(user_max)
#
# users = [user_kira, user_kira, User('Kokos', 2, 0)]
#
# print(users)


# class User:
#     __count = 0
#
#     def __init__(self, name, age):
#         self.__name = name
#         self._age = age
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#
# user = User("Max", 15)
# # print(user.get_name())
# # user.set_name('Olha')
# # print(user.get_name())
# # # print(User.__count)
# print(User._User__count)
# print(user._User__name)


# class Car:
#     def __init__(self, color, speed, brand):
#         self.color = color
#         self.speed = speed
#         self.brand = brand
#
#     def start(self):
#         print('Start')
#
#     def greeting(self):
#         print("Hello World1")
#
#
# class Tools:
#     def greeting(self):
#         print("Hello World2")
#
#
# class ElectricCar(Car, Tools):
#     def __init__(self, color, speed, brand, battery):
#         super().__init__(color, speed, brand)
#         self.battery = battery
#
#
# car = ElectricCar("red", 200, 'Kia', 1000)
# car.start()
#
# car.greeting()


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def __get_name(self):
#         return self.__name
#
#     def __set_name(self, name):
#         if len(name) > 4:
#             self.__name = name
#
#     def __del_name(self):
#         del self.__name
#
#     def __str__(self):
#         return f'{self.__dict__}'
#
#     name = property(fget=__get_name, fset=__set_name, fdel=__del_name)


# user = User('Max')
# print(user)
# user.house = 25
# user.house = 30
# user.age = 25
# del user.house
# print(user)


# user = User('Max')
# print(user.get_name())
# user.set_name("Kira")
# print(user.get_name())
# user.del_name()
# print(user)
# print(user.get_name())

# user = User('Max')
#
# user.name = "Kiraddd"
#
# print(user.name)

# del user.name
# print(user.name)


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if len(name) > 4:
#             self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     def __str__(self):
#         return f'{self.__dict__}'
#
#
# user = User('Max')
#
# user.name = "Kira"
#
# print(user.name)
# #
# del user.name
# print(user.name)


# class Shape:
#     def area(self):
#         pass
# 
#     def perimeter(self):
#         pass
# 
# 
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
# 
#     def area(self):
#         return self.a + self.b / self.c
# 
#     def perimeter(self):
#         return self.a + self.b + self.c
# 
# 
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
# 
#     # def area(self):
#     #     return self.a * self.b
# 
#     def perimeter(self):
#         return 2 * (self.a + self.b)
# 
# 
# shapes: list[Shape] = [
#     Triangle(1, 2, 3),
#     Triangle(2, 3, 4),
#     Rectangle(2, 3)
# ]
# 
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimeter())


from abc import ABC, abstractmethod


class Shape:
    # @abstractmethod
    def area(self):
        pass

    # @abstractmethod
    def perimeter(self):
        pass


# shape = Shape()
# print(shape)

class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return self.a * self.b - self.c

    def perimeter(self):
        return 2 * (self.a + self.b) + self.c


# class Rectangle(Shape):
#     def area(self):
#         return 2 * (self.a + self.b)
#
#     # def perimeter(self):
#     #     return self.a * self.b
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
# triangle = Triangle(1, 2, 3)
# shapes: list[Shape] = [
#     Triangle(1, 2, 3),
#     Triangle(2, 3, 4),
#     Rectangle(2, 3)
# ]
#
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimeter())
#

# from typing import Self
#
#
# class User:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def __add__(self, other: Self):
#         return self.age + other.age
#
#     def __sub__(self, other: Self):
#         return self.age - other.age
#
#     def __len__(self):
#         return len(self.name)
#
#     def __mul__(self, other: Self):
#         return self.age * other.age
#
#     def __gt__(self, other: Self):
#         return self.age > other.age
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#     def __eq__(self, other: Self):
#         return self.age == other.age
#
#
# user1 = User("Max", 5)
# user2 = User("Karina", 10)
# user3 = User("Albina", 10)
#
# print(user1 + user2)
# print(user1 - user2)
# print(user1 * user2)
# print(user1 < user2)
# print(user1 > user2)
#
# print(len(user1))


# class User:
#     __count = 1
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     @staticmethod
#     def greeting():
#         print('Hello')
#
#     @classmethod
#     def get_count(cls):
#         cls.__count+=1
#         print(cls.__count)
#
#
# # user = User("Max")
# # user.greeting()
# # User.greeting()
# User.get_count()

# class User:
#     def __init__(self, name):
#         self.name = name
#
#
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author


# user = User("Max")
# book = Book("hsdgfjh", 'dddd')
#
# print(isinstance(user, User))

# class User:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not isinstance(cls.__instance, cls):
#             cls.__instance = super().__new__(cls)
#
#         return cls.__instance
#
#     def __init__(self, name):
#         self.name = name
#
#
# user = User("Max")
# user2 = User("Kira")
#
# print(user.name)
# print(user2.name)


# class Prod:
#     def __init__(self, value):
#         self.value = value
#
#     def __call__(self, item):
#         return self.value * item
#
#
# prod = Prod(125)
# print(prod.value)
# prod(3)
# print(prod(2))

class Array:
    def __init__(self, *args):
        self.__arr = [*args]

    def __str__(self):
        return str(self.__arr)

    @property
    def length(self):
        return len(self.__arr)

    def __setitem__(self, key, value):
        self.__arr[key] = value

    def __getitem__(self, key):
        return self.__arr[key]

    def __delitem__(self, key):
        del self.__arr[key]

    def push(self, item):
        self.__arr.append(item)

    def map(self, cb):
        return Array(*[cb(item) for item in self.__arr])

    def filter(self, cb):
        return Array(*[item for item in self.__arr if cb(item)])


arr = Array(1, 2, 3, 22, 66, 88)

print(arr)
print(arr.length)

arr[2] = 555
print(arr)
print(arr[0])
del arr[0]
print(arr)

arr.push(999)
print(arr)

arr_map = arr.map(lambda x: x * 2)
print(arr_map)

print(arr.filter(lambda x: x < 5))
