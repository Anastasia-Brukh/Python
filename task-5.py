#автор Анастасия Брух
# Задача-5: Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен
# разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rating = [7, 4, 3, 2]
print("Существует Рейтинг: ", rating)
number = int(input("Введите число для рейтинга: "))
c = rating.count(number)
for element in rating:
    if c > 0:
        i = rating.index(number)
        rating.insert(i+c, number)
        break
    else:
        if number > element:
            j = rating.index(element)
            rating.insert(j, number)
            break
        elif number < rating[len(rating) - 1]:
            rating.append(number)
print("Измененный Рейтинг: ", rating)