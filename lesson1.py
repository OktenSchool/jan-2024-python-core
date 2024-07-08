# kjdfjfjfj

"""
kjsfhksjf
jsdhfksfh

"""

'''
sdfhskfjhsf
jsdhfksfd
'''

# print(1,2,3, sep='-', end='finish!!!\n')

# i = 3
# f = 1.2
# b = True  # False
# s = 'text' # "text"
# n = None
#
# print(type(i))
# print(type(f))
# print(type(b))
# print(type(s))
# print(type(n))
#
# a=b=c=d=10
#
# print(a, b, c, d)
#
# print([int('125')])
# print([float(1)])
# print([bool('')])
# print([str(25)])
#
# s = '*'*20
#
# print(s)

# a=0

# a++
# ++a
# a+=1
# a=a+1


a = 6
b = 2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)
# print(2525**2525)

# str = input('Enter number:')
#
# print(str)

# print(a<b)
# print(a>b)
# print(a>=b)
# print(a<=b)
# print(a==b)
# print(a!=b)
# print(a is b)
# print(a is not b)

# s = 'string'
#
# print(isinstance(s, str))
a = 5
b = 9
# if (a<b or and a>b):

# if a<b:
#     kjdfkjsf
#     jshdfkjfh
#     lsjdfkjhf

# num = int(input('Enter num: '))

# if num <5:
#     print('num <5')
# elif num>10:
#     print('num>10')
# else:
#     print('no')

# res = 'yes' if num >5 else 'no'
#
# print(res)


# l = [1, 2, 3, 4, 5, 6]
# print(l[88])
# print('!!!!!!!!!!!')

# l2 = l
# l2 = l.copy()
# print(l[-2])

# l.append(23)
# l.insert(155, 55)
# print(l)

# del l[1]
# l = [1, 2, 3, 4, 5, 6,2]
# pop = l.pop()
# pop = l.pop(2)
# print(l)
# print(pop)
# l.remove(2)
#
# print(l)

# l1 = [12,3,4, 4,5,6,7,8,9,2,3,4]
# l2 = [55,32,43]
#
# # l1.extend(l2)
# #
# # print(l1)
#
# l1 += l2
# print(l1)

# print(l1.index(4,5, 9))
# print(l1.index(55555))

# l1 = [12,3,4, 4,5,6,7,8,9,2,3,4]
# # l1.sort()
# # l1.sort(reverse=True)
# # print(l1)
# # print(l1.count(4))
# l1.clear()

# l2 = l1[::-2]
# print(l2)

# tuple

# my_tuple = (5, 4, 6, 7)
# del  my_tuple[2]
# my_tuple[2]=44


dictionary = {
    'name': 'Max',
    'age': 18,
}

# print(dictionary['name'])
# dictionary['name'] = 'Olha'
# dictionary['234']='456'
# # print(dictionary['ddddd'])
# del dictionary['age']

# dictionary.clear()

# print(dictionary.get('age2', 55))
# print(dictionary)
# print(dictionary.items())
# print(dictionary.keys())
# print(dictionary.values())
# print(dictionary.pop('name'))
# dictionary.popitem()
# dictionary.setdefault('name', 25)
# print(dictionary)
#
# asd = {
#     'house': '55',
# }
#
# # dictionary.update(asd)
# dictionary |= asd
#
# print(dictionary)


# l = [1, 2, 3, 3, 2, 4, 1]
#
# s = set(l)
# print(s)

# s = set()
# print(type(s))
# s.add(2)
# s.add(3)
# s.add(5)
# s.add(2)
#
# print(s)

# s1 = {1,2,3,4,5,6,7,8}
# s2 = {11, 25, 15, 8}
#
# print(s1.issuperset(s2))
# print(s1.isdisjoint(s2))
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))
#
# # s1.remove(55)
# # s1.discard(55)
# s1.pop()
# print(s1)

# string = 'name = Vasia \'sd\'fhf\' '
#
# print(string)
name = 'Max'
age = 18
weight = 70.5
# # string = 'Hello, my name is Max, I`m 18 and my weight 70.5 kg'
# # string = 'Hello, my name is '+name+', I`m '+str(age)+' and my weight '+str(weight)+' kg'
# string = 'Hello, my name is %s, I`m %d and my weight %f kg' %(name, age, weight)
# string = 'Hello, my name is {}, I`m {} and my weight {} kg'.format(name, age, weight)
# string = 'Hello, my name is {name}, I`m {age} and my weight {weight} kg'.format(name=name, weight=weight, age=age)
string = f'heello, my name is {name}, I`m {age} and my weight {weight} kg'

#
# print(string)

# string.index('lfdg')
# string.count()
# print(string)
# print(string.capitalize())
# print(string.upper())
# print(string.title())
#
# string.startswith('')
# string.endswith('')
#
# print('hello-world'.split('-'))
# print('hello-is-world'.partition('is'))
# print(['  hello-world    a'.strip('a ')])
# # print(['  hello-world    '.rstrip()])
# # print(['  hello-world    '.lstrip()])
#
# strs = ['hello', 'world', 'is', 'is-world']
# print('-'.join(strs))
#
# string = string.replace('e', '55')
# print(string)
# print(string[::2])


# print(min(3, 5, -4, 6))
# print(min([3, 5, -4, 6]))
# print(max([3, 5, -4, 6]))
# print(sum([3, 5, -4, 6]))
# print(sorted([3, 5, -4, 6]))
# print(sorted([3, 5, -4, 6], reverse=True))
# print(pow(2,5))


# def func(a, b, c, d=5, *args, **kwargs):
#     print(a,b,c,d,)
#     print(args)
#     print(kwargs)
#
#
# func(1,2,3,55,3,4,8,9, name='Max', age=15)

# i = 5
# while i>0:
#     i-=1
#     if i ==2:
#         continue
#     print(i)
# else:
#     print('end while')

# l = [1,2,3,4,5]
#
# for item in l:
#     print(item)
# else:
#     print('end for')


# for i in range(5, 20, 2):
#     print(i)


# l = ['max', 'olha', 'viktor', 'kesha']
#
# for i,v in enumerate(l):
#     print(f'{i=}')
#     print(f'{v=}')

# dict_ = {
#     'name': 'max',
#     'age': 18,
# }
#
# for key, value in dict_.items():
#     print(key)
#     print(value)

# list comprehension


l = [1, 2, 3, 4, 5, 6]

# res = [i**2 for i in l if i % 2 == 0]
# res = [i for i in range(50)]
# res = [i**2 for i in l]
# res = ['even' if i%2==0 else 'odd' for i in l]
# print(res)


dict1 = {'Name': 'vasia', 'aGe': 13}

dict2 = {k.lower(): v for k, v in dict1.items()}

print(dict2)

l1 = [1,2,3,4]
l2 = l1

# print(l1 is l2)

l3 = []

if not l3:
    print('full')