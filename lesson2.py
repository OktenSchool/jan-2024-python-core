# l = [1, 2, 3, 5,4,5,6,]

# a,b,c = l

# _,_,c =l
# _,a,*_ = l
# print(a, _)


# a = 5
# b = 9
#
# a, b = b, a
#
# print(a, b)

# d = {
#     'arg1': 4,
#     'arg2': 5,
#     'arg3': 6,
# }
#
# l = [6,7,8]
# def func(arg1, arg2, arg3):
#     print(arg1, arg2, arg3)
#
#
# # func(d['arg1'], d['arg2'], d['arg3'])
#
# func(*l)

# def decor_star(func):
#     def inner(*args, **kwargs):
#         print('*' * 20)
#         func(*args, **kwargs)
#         print('*' * 20)
#
#     return inner
#
# def decor(func):
#     def inner(*args, **kwargs):
#         print('-' * 20)
#         func(*args, **kwargs)
#         print('-' * 20)
#
#     return inner
# @decor
# @decor_star
# def greeting(name):
#     print(f"Hello, {name}!")
#
#
# # inner = decor_star(greeting)
# # inner("max")
#
# greeting(name='John')


# for i in range(5):
#     print(i)
#
# print(i)

# a=5
# name ='Max'
#
#
# def func():
#     name = "Olha"
#     print(locals())
#
#
#
# print(globals())
# func()


# name = 'Max'
#
#
# def a():
#     global name
#     name = 'Oleg'
#
#     def b():
#         name = 'Kira'
#
#         def c():
#             name = 'Petro'
#             print(name)
#
#         print(name)
#         c()
#
#     print(name)
#     b()
#
#
# a()
# print(name)


# name = 'Max'
#
#
# def a():
#     # name = 'Oleg'
#
#     def b():
#         # name = 'Kira'
#
#         def c():
#             nonlocal name
#             # name = 'Petro'
#             print(name)
#
#         print(name)
#         c()
#
#     print(name)
#     b()
#
#
# a()
# print(name)

# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#
#     return inner
#
#
# conter1 = counter()
# conter2 = counter()
#
#
# conter1()
# conter2()
# conter2()
# conter1()
# conter1()
# conter2()
# conter1()


# const = func =(a,b)=>a+b
# const = func =(a,b)=>{
#
# }

# func = lambda a,b: a+b
#
# print(func(1, 2))

# users = [
#     {'name': 'Max', 'age': 18},
#     {'name': 'Kira', 'age': 25},
#     {'name': 'Alina', 'age': 20},
#     {'name': 'Kiril', 'age': 30},
# ]
#
# users.sort(key=lambda item: item['name'])
#
# print(users)

# l = [2, 3, 6, 4, 2, 5, 1, 0]
#
# m = map(lambda x: str(x), l)
# list1 = list(m)
# print(list1)
# # for i in m:
# #     print([i])
# #
# # for i in m:
# #     print([i])
#
# f = filter(lambda x: x % 2 == 0, l)
#
# # print(list(f))
#
# def asd1(name: list[str]):
#     pass
#
#
# def asd2(name: tuple[str, int, bool]):
#     pass
#
#
# def asd3(name: tuple[str, ...]):
#     pass
#
#
# def asd4(name: tuple[str, ...]) -> None:
#     name = 5
#
#
# MyType = None | int | bool
#
#
# def asd4(name: tuple[str, ...]) -> MyType:
#     name = 5
#     return 5
#
#
# asd(('ss', 'ddd', 'dddd'))

# import typing
from typing import Callable, NewType, TypedDict

# def counter() -> Callable[[str, int], bool]:
#     count = 0
#
#     def inner(a: str, b: int) -> bool:
#         nonlocal count
#         count += 1
#         print(count)
#         return True
#
#     return inner

# UserId = NewType('UserId', int)
#
#
# def func(user: UserId):
#     pass
#
#
# func(UserId(222))

UserType = TypedDict('UserType', {'name': str, 'age': int, 'house': int, 'status': bool}, total=False)

users: list[UserType] = [
    {'name': 'Max', 'age': 15, 'house': 25, 'asd': 15},
    {'name': 'Max', 'age': 15, 'house': 25, 'status': True},
    {'name': 'Max', 'age': 15, 'house': 25, 'status': True},
]

user: UserType = {'name': 'Max', 'age': 15, 'house': 25, 'asd': 15}
