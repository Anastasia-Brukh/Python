# автор Анастасия Брух
"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат. """


class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f' {self.name} движется.'

    def stop(self):
        return f'\n {self.name} остановилась.'

    def turn(self, direction):
        return f'\n {self.name} поворот на {direction}'

    def show_speed(self):
        return f'\nСкорость автомобиля {self.speed}'

class TownCar(Car):
    def show_speed(self):
        # def __init__(self, speed, color, name, is_police):
        #     super().__init__(speed, color, name, is_police)
        if self.speed > 60:
            return f'\nВы превысили скорость! Ваша скорость {self.speed}'
        else:
            return f'Скорость {self.name} согласно правилам'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\n Вы превысили скорость! Ваша скорость {self.speed}!'
        else:
            return f'Скорость {self.name} согласно правилам.'

class PoliceCar(Car):
    pass


town = TownCar('Toyota', 70, 'Черный', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('Лево.'), town.turn('Право.'), town.stop())

sport = SportCar('BMW', 190, 'Серебристый', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('Право.'), sport.stop())

work = WorkCar('JCB', 30, 'Желтый', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('Право.'), work.stop())

police = PoliceCar('Hundai', 100, 'Белый', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())


