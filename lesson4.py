# try:
#     jhsdfjhsfh
# except Exception:
#     print("NameError")
# print('end')
# try:
#     print('start')
#     # ddddd
#     res = 100/0
# except ZeroDivisionError:
#     print('ZeroDivisionError')
# except NameError:
#     print('NameError')
# else:
#     print('all ok')
# finally:
#     print('finally')

# def func():
#     arr = []
#     for i in range(10):
#         arr.append(i + 1)
#
#
# print('start')
# func()
# print('end')


# l = [i for i in range(50_000_000)]
# input()

# g = (i for i in range(50_000_000))
# print(type(g))
# #
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
#
# for i in g:
#     print(i)

# def gen(name):
#     for ch in name:
#         yield ch
#         print('Hello')
#
#
#
# g = gen("Name")
#
# print(next(g))
# print(next(g))
# # print(next(g))
# # print(next(g))


# def gen():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#     return 'retsdfsdfsfdurn'
#
#
# g = gen()
# try:
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
# except StopIteration as e:
#     print(e)

# def gen1(n):
#     for i in range(1, n + 1):
#         yield f'{i}-Team1'
#
#
# def gen2(n):
#     for i in range(1, n + 1):
#         yield f'{i}-Team2'
#
#
# teams = [gen1(8), gen2(5)]
#
# while teams:
#     player = teams.pop(0)
#
#     try:
#         print(next(player))
#         teams.append(player)
#     except StopIteration:
#         pass

import uuid


#
#
def gen_jpeg_file_name():
    pattern = '{}.jpg'
    count = 0
    while True:
        count += 1
        yield pattern.format(f'{uuid.uuid1()}{count}')


g = gen_jpeg_file_name()
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# class MyRange:
#     def __init__(self, length):
#         self.__length = length
#         self.__counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__counter < self.__length:
#             res = self.__counter
#             self.__counter += 1
#             return res
#         raise StopIteration

# def my_range(length):
#     count = 0
#     while count < length:
#         yield count
#         count += 1
#
#
# for i in my_range(10):
#     print(i)
# try:
#     file = open('111.txt')
#     try:
#         print(file.read())
#     finally:
#         file.close()
# except Exception as err:
#     print(err)


# try:
#     with open('111.txt', 'r') as file:
#         # print(file.read())
#         # print(file.readlines())
#         # print(file.readline())
#         # print(file.readline())
#         # print(file.readline())
#         # print(file.readline())
#         # print(file.readline())
#         # print(file.readline())
#         # print(file.readline())
#         for line in file:
#             print(line)
# except Exception as err:
#     print(err)

# try:
#     with open('222.txt', 'w') as file:
#         # file.write('Hello\nWorld\nPython')
#         file.writelines(['asd\n', 'fgh\n', 'tyu\n'])
# except Exception as err:
#     print(err)


# try:
#     with open('222.txt', 'a') as file:
#         file.write('!!!!!!!!!!!!!!!\n')
# except Exception as err:
#     print(err)

# try:
#     with open('2223.txt', 'x') as file:
#         pass
# except Exception as err:
#     print(err)

# try:
#     with open('222.txt', 'r+') as file:
#         print(file.read())
#         file.write('End\n')
# except Exception as err:
#     print(err)

# try:
#     with open('222.txt', 'w+') as file:
#         # print(file.read())
#         file.write('End\n')
#         # file.seek(0)
#         print(file.read())
# except Exception as err:
#     print(err)

# try:
#     with open('222.txt', 'w+') as file:
#         # print(file.read())
#         file.write('End\n')
#         # file.seek(0)
#         print(file.read())
# except Exception as err:
#     print(err)

# try:
#     with open('images.jpeg', 'rb') as file, open('copy.jpeg', 'wb') as file2:
#         file2.write(file.read())
# except Exception as err:
#     print(err)

# try:
#     with open('images.jpeg', 'rb') as file:
#         read = file.read()
#         for _ in range(50):
#             with open(next(g), 'wb') as file2:
#                 file2.write(read)
# except Exception as err:
#     print(err)

import json, pickle

from typing import TypedDict

User = TypedDict('User', {'name': str, 'age': int, 'status': bool})

user: User = {
    'name': "max",
    'age': 30,
    'status': True
}


# try:
#     with open('users.json', 'w') as f:
#         json.dump(user, f)
# except Exception as err:
#     print(err)


# try:
#     with open('users.json', 'r') as f:
#         user:User = json.load(f)
#         print(user['name'])
# except Exception as err:
#     print(err)

# try:
#     with open('users.data', 'wb') as f:
#         pickle.dump(user, f)
# except Exception as err:
#     print(err)


# try:
#     with open('users.data', 'rb') as f:
#         user:User = pickle.load(f)
#         print(user['name'])
# except Exception as err:
#     print(err)


# try:
#     with open('users.txt', 'w') as f:
#         print('Hello', file=f)
# except Exception as err:
#     print(err)


# i = 'sss'
#
# match i:
#     case 'a':
#         print('a')
#     case 'b':
#         print('b')
#     case _:
#         print('default')

# p = ['top', '200']
#
# match p:
#     case 'left'|'top', step:
#         print('left', step)
#     case 'right' as action, step:
#         print(action, step)


class User:
    __match_args__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


user_class = User("kokos", 30)

user_dict = {'name': 'Karina', 'age': 40}


# def matcher(source: User | dict):
#     if isinstance(source, User):
#         print(source.name)
#     elif isinstance(source, dict):
#         print(source['name'])
#
# matcher(user_class)

def matcher(source: User | dict):
    match source:
        case User('kokos' as name, age):
            print(name, age)
        case {'name': str(name), 'age': int(age)}:
            print(name, age)


matcher(user_class)
