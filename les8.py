# 1. Написать класс Student
# Конструктор класса принимает аргументы: first_name: str, group: int, marks: list[int]
# Написать метод __str__ возвращающая форматированную строку с данными об студенте
# Написать функцию (не метод) student_sort принимающая список студентов: students:
# list[Student] и возвращающая список студентов отсортированный по имени



# class Student:
#     def __init__(self, first_name: str, group: int, marks: list[int]):
#         self.first_name = first_name
#         self.group = group
#         self.marks = marks
#     def __str__(self):
#         self.line = "Оценки студента {} группы {} \n{}".format(self.first_name, self.group, self.marks)
#         return self.line
# def student_sort(students: list[Student]) -> list[str]:
#     sort = sorted(students)
#     return sort
#
#
# Vadim = Student('Вадим', 101117, [2, 3, 4, 5])
# Andrey = Student('Андрей', 103127, [4, 10, 8, 6])
# Larisa = Student('Лариса', 101137, [9, 10, 8, 9])
# # x = student_sort([Vadim.first_name, Andrey.first_name, Larisa.first_name])
# print(Andrey)
# print(sorted(student_sort([Vadim.first_name, Andrey.first_name, Larisa.first_name])))




# 2. Написать класс Rectangle
# Конструктор класса принимает координаты точек по диагонали (правая нижняя, верхняя
# левая или левая нижняя, правая верхняя)
# Написать метод perimeter возвращающий периметр получившегося прямоугольника
# Написать метод square возвращающий площадь получившегося прямоугольникаы
# *учесть, что координаты на плоскости могут быть отрицательными
#
class Rectangle:
    def __init__(self, coordinates1: list, coordinates2: list ) -> None:
        self.coordinates1 = coordinates1
        self.coordinates2 = coordinates2

    def perimeter(coordinates1: list, coordinates2: list) -> float:
        bias_x = abs(float(coordinates1[0]) - float(coordinates2[0]))
        bias_y = abs(float(coordinates1[1]) - float(coordinates2[1]))
        perimeter = 2 * bias_x + 2 * bias_y
        return perimeter
    # def square(self):


a = Rectangle.perimeter(coordinates1=[-6, 2], coordinates2=[5, -3])
print(a)



# 3. Написать класс Numbers
# Конструктор класса принимает список чисел numbers: list[int]
# Написать метод average — возвращающий среднее арифметическое между всеми числами
# Написать метод max_count — возвращающий число из списка, которое чаще встречается,
# если таких чисел несколько, вывести среднее арифметическое среди таких чисел