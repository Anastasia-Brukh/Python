# автор Анастасия Брух
# Задача-1: Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_int = 5
my_float = 1.2
my_str = "Выполнение домашнего задания"
my_list = ['a', '2']
my_tuple = ('b', '3')
my_dict = {'Столица России': 'Москва', 'Столица США': 'Вашингтон'}

list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in list:
    print(f'{i} это {type(i)}')
