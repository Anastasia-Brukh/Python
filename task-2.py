"""" автор Анастасия Брух
Задание 2: Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
 Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
 Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
 Результат: [12, 44, 4, 10, 78, 123]."""


in_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_list = [number for i, number in enumerate(in_list) if i > 0 and in_list[i] > in_list[i - 1]]
print(res_list)
"""Вариант 2"""
res_list = [num1 for num1, num2 in zip(in_list[1:], in_list[:]) if num1 > num2]
print(res_list)