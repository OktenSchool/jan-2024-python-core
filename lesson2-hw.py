# from typing import Callable
#
#
# # def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
# def notebook():
#     todo_list: list[str] = []
#
#     def add_todo(todo: str) -> None:
#         nonlocal todo_list
#         todo_list.append(todo)
#
#     def get_all() -> list[str]:
#         nonlocal todo_list
#         return todo_list.copy()
#
#     return add_todo, get_all
#
#
# add, all = notebook()
# #
# # add('dddddd')
# # add('llll')
# #
# # print(all())
#
# l = all()
# l.append('ddddddddddddd')
#
# print(all())


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'


# def expanded_form(num: int) -> str:
#     st = str(num)
#     length = len(st) - 1
#     res = []
#     for i, ch in enumerate(st):
#         if ch != '0':
#             res.append(ch + '0' * (length - i))
#     return f"{' + '.join(res)} = {st}"
#
#
# print(expanded_form(25025))


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій

def count_decor(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        func(*args, **kwargs)
        print(f'{count=}')

    return inner


@count_decor
def func1():
    print('func1')


@count_decor
def func2():
    print('func2')

func1()
func1()
func2()
func1()
func2()

