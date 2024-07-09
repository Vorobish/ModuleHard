from math import sqrt
from math import pi

class Figure:
    sides_count = 0
    name = 'фигура'

    def __init__(self, sides_count, sides, color):
        if self.__is_valid_sides(len(sides), sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count
        if self.__is_valid_color(*color):
            self.__color = color
        else:
            self.__color = [255, 255, 0]  # по умолчанию - желтый  # FFFF00

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False    #new 1

    def __is_valid_sides(self, s, *sides):
        list_ = list(*sides)
        sp = 0
        if len(list_) == 1 and list_[0] > 0:
            sp = 1 * self.sides_count
        else:
            for i in list_:
                if i > 0:
                    sp += 1
        if s == self.sides_count and s == sp:
            return True
        else:
            return False

    def set_sides(self, *sides):
        if self.__is_valid_sides(len(sides), sides):
            self.__sides = list(sides)
            self.recalculation_value()

    def get_sides(self):
        return self.__sides

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color


    def __len__(self):
        return self.P

    def say_info(self):
        print(f'Фигура: {self.name}, кол-во сторон {self.sides_count}, стороны: {self.__sides}, цвет: {self.__color}'
              f', периметр: {self.P}', end=' ')


class Circle(Figure):
    name = 'круг'
    sides_count = 1

    def __init__(self, color, *sides):  # filled(закрашенный, bool)
        super().__init__(Circle.sides_count, list(sides), list(color))
        self.get_P()
        self.get_r()
        self.get_square()
        self.say_info()

    def recalculation_value(self):
        self.get_P()
        self.get_r()
        self.get_square()

    def get_P(self):
        self.P = int(self.get_sides()[0])
        return self.P

    def get_r(self):
        self.__radius = int(self.get_sides()[0]) / (2 * pi)
        return self.__radius

    def get_square(self):
        self.S = pi * self.__radius ** 2
        return self.S

    def say_info(self):
        super().say_info()
        print(f', радиус {self.__radius.__round__(2)}, длина окружности {self.get_sides()}, площадь {self.S.__round__(2)}')


class Triangle(Figure):
    name = 'треугольник'
    sides_count = 3

    def __init__(self, color, *sides):  # filled(закрашенный, bool)
        super().__init__(self.sides_count, list(sides), list(color))
        self.get_P()
        self.get_h()
        self.say_info()

    def recalculation_value(self):
        self.get_P()
        self.get_h()
        self.get_square()

    def get_square(self):
        self.S = self.a * self.__height / 2
        return self.S

    def get_P(self):
        self.P = sum(self.get_sides())
        return self.P

    def get_h(self):
        self.a = int(self.get_sides()[0])
        self.b = int(self.get_sides()[1])
        self.c = int(self.get_sides()[2])
        self.p = sum(self.get_sides()) / 2
        self.__height = (2 * sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))) / self.a
        return self.__height

    def say_info(self):
        super().say_info()
        print(f', высота {self.__height.__round__(2)}, площадь {self.S.__round__(2)}')


class Cube(Figure):
    name = 'куб'
    sides_count = 12

    def __init__(self, color, *sides):  # filled(закрашенный, bool)
        super().__init__(self.sides_count, list(sides * 12), list(color))
        self.get_P()
        self.get_volume()
        self.say_info()

    def recalculation_value(self):
        self.get_P()
        self.get_volume()

    def get_P(self):
        self.P = sum(self.get_sides())
        return self.P

    def get_volume(self):
        self.V = self.get_sides()[0] ** 3
        return self.V

    def say_info(self):
        super().say_info()
        print(f', объем {self.V.__round__(2)}')


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

circle1.say_info()
cube1.say_info()

