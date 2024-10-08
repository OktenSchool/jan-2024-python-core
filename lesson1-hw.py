# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
# st = 'as 23 fdfdg544'
#
# print(','.join(num for num in st if num.isdigit()))

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
# st = 'as 23 fdfdg544 34'

# print(', '.join(''.join(ch if ch.isdigit() else ' ' for ch in st).split()))

# 1)є строка:
greeting = 'Hello, world'


# записати кожний символ як окремий елемент списку і зробити його заглавним:

# print([ch.upper() for ch in greeting])


# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# print([i**2 for i in range(50)  if i % 2])


def show_list(arr):
    print(arr)


def max_n(a, b, c):
    max_num = max(a, b, c)
    print(max_num)
    return max_num


def min_max(*args):
    print(max(args))
    return min(args)


def max_of_list(arr):
    return max(arr)


def min_of_list(arr):
    return min(arr)


def sum_of_list(arr):
    return sum(arr)


def average_of_list(arr):
    return sum(arr) / len(arr)


# 1)Дан list:
list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# 3) вывести табличку множення за допомогою цикла while
# 4) переробити це завдання під меню


def duplicate():
    l = list1.copy()
    print(list(set(l)))


def to_x():
    l = list1.copy()
    print(['X' if not (i + 1) % 4 else item for i, item in enumerate(l)])


def square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')


def multi_table():
    size = 9
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            res = i * j
            # print(' ' if res//10 else '  ', end='')
            # print(res, end='')
            print(f'{res:3}', end='')
            j += 1
        print()
        i += 1


while True:
    print('1) знайти мін число')
    print('2) видалити усі дублікати')
    print('3)  замінити кожне 4-те значення на \'X\'')
    print('4) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції')
    print('5) вывести табличку множення за допомогою цикла while')
    print('9) Вихіх')

    choice = input('Зробіть свій вибір: ')

    if choice == '1':
        print(min_of_list(list1))
    elif choice == '2':
        duplicate()
    elif choice == '3':
        to_x()
    elif choice == '4':
        square(5)
    elif choice == '5':
        multi_table()
    elif choice == '9':
        break
