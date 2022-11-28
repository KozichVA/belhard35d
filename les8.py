# # 1. Написать класс Student
# # Конструктор класса принимает аргументы: first_name: str, group: int, marks: list[int]
# # Написать метод __str__ возвращающая форматированную строку с данными об студенте
# # Написать функцию (не метод) student_sort принимающая список студентов: students:
# # list[Student] и возвращающая список студентов отсортированный по имени
#
#
#
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
# print(sorted(student_sort([Vadim.first_name, Andrey.first_name, Larisa.first_name])), end='\n\n\n')
#
#
#
# # 2. Написать класс Rectangle
# # Конструктор класса принимает координаты точек по диагонали (правая нижняя, верхняя
# # левая или левая нижняя, правая верхняя)
# # Написать метод perimeter возвращающий периметр получившегося прямоугольника
# # Написать метод square возвращающий площадь получившегося прямоугольникаы
# # *учесть, что координаты на плоскости могут быть отрицательными
# #
# # class Rectangle:
#
#     # def square(self):    # def __init__(self, coordinates1: list, coordinates2: list ) -> None:
# #     #     self.coordinates1 = coordinates1
# #     #     self.coordinates2 = coordinates2
# #     #
# #     # def perimeter(self, coordinates1: list, coordinates2: list) -> float:
# #     #     bias_x = abs(float(coordinates1[0]) - float(coordinates2[0]))
# #     #     bias_y = abs(float(coordinates1[1]) - float(coordinates2[1]))
# #     #     perimeter = 2 * bias_x + 2 * bias_y
# #     #     return f"Периметр прямоугольника = {perimeter} мм."
# #
# # a = Rectangle.perimeter(coordinates1=[-6, 2], coordinates2=[5, -3])
# # print(a)
# class Rectangle:
#     def __init__(self, coordinate1: list, coordinate2: list) -> None:
#         self.X1 = float(coordinate1[0])
#         self.X2 = float(coordinate2[0])
#         self.Y1 = float(coordinate1[1])
#         self.Y2 = float(coordinate2[1])
#
#     def get_perimeter(self) -> str:
#         bias_x = abs(self.X2 - self.X1)
#         bias_y = abs(self.Y2 - self.Y1)
#         return f"Периметр прямоугольника = {(bias_x + bias_y) *2} мм."
#
#     def get_square(self) -> str:
#         bias_x = abs(self.X2 - self.X1)
#         bias_y = abs(self.Y2 - self.Y1)
#         return f"Площадь прямоугольника = {(bias_x * bias_y)} мм^2."
#
# point_A = [-6, 2]
# point_C = [5, -3]
# AC = Rectangle(point_A, point_C)
# print(AC.get_perimeter())
# print(AC.get_square())
#     # 3. Написать класс Numbers
# # Конструктор класса принимает список чисел numbers: list[int]
# # Написать метод average — возвращающий среднее арифметическое между всеми числами
# # Написать метод max_count — возвращающий число из списка, которое чаще встречается,
# # если таких чисел несколько, вывести среднее арифметическое среди таких чисел
#
# class Number:
#     suma = 0
#     def __init__(self, numbers: list[int]):
#         self.num = numbers
#
#     def get_average(self) -> float:
#         for i in range(len(self.num)):
#             self.suma += self.num[i]
#         self.suma = self.suma / i
#         return f'\nсреднее арифметическое = {self.suma}'
#
#     def max_count(self):
#
#         self.how_many = 1   #сколько чисел в списке имеет одинаковое количество повторений
#         self.max = 1        #наибольшее количество повторений i-ого числа
#         print('т.к. в начале ничего не делаем всегда, со старта нужно присвоить какой-то переменной num[0] ')
#         for i in range(len(self.num)):
#             if self.num.count(i) == self.max:
#                 self.how_many += 1
#                 print(f'на {i}-ой складывам i-e числа а делить будем на {self.how_many}, но это за переделами цикла')
#             elif self.num.count(i) > self.max:
#                 self.max += 1
#                 self.how_many = 1
#                 print(f'''на {i}-ой удаляем сумму чисел и присваем новое i-ое значение = {self.num[i - 1]} + обновляем max,''')
#
#             else:
#                 print(f'на {i}-ой ничего не делаем')
#
#
#
#
#
#         #     self.max = self.num.count(i)
#         #     if self.max >= self.repetition:
#         #         self.repetition = self.max
#         #         rezalt = self.num[i]
#         #         print(f'{rezalt} на {i}-ом шаге')
#         #         # if self.max == self.repetition:
#         #         #     self.how_many += 1
#         #         #     rezalt += self.num[i]
#         #         #     rezalt = rezalt / self.how_many
#         #         #     print(f'аримитическое {rezalt} на {i}-ом шаге')
#         # return rezalt
#
# print(Number([1, 2 ,3]).get_average(), end = '\n\n')
# print(Number([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 5, 6, 7, 10]).max_count())

# def DNA_strand(dna: str) -> str:
#     # code here
#     rezalt = ''
#     complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
#     for key in dna:
#         rezalt += complements[key]
#     return rezalt
#
# print(DNA_strand('GTAT'))

# def accum(s):
#     # your code
#     rezalt = []
#     for i in range(len(s)):
#         letter = s[i]*(i+1)
#         rezalt.append(letter.capitalize())
#     return '-'.join(rezalt)
#
#
# print(accum('asdgjsad'))

# def solution(s):
#     rezult =[]
#     i = 0
#     while i <= len(s):
#         rezult.append(s[i: (i + 2)])
#         i += 2
#     if len(s) % 2:
#         rezult.append(rezult.pop() + '_')
#     else:
#         rezult.remove('')
#     return rezult
#
# print(solution('abcdefgre'))



# def array_diff(a, b):
    #your code here
    # for i in range(len(b)):
    #     while a.count(b[i]):
    #         a.remove(b[i])
    # return a
# def array_diff(a, b):
#     return [x for x in a if x not in b]
#
# print(array_diff([1,2,2,2,2,3], [2]))

# def get_sum(a,b):
#     #good luck!
#     if a < b:
#         A = a
#         B = b
#     else:
#         A = b
#         B = a
#     return sum([*range(A, B + 1)]) if a != b else a
# print(get_sum(1, 5))




# def is_pangram(s: str) -> bool:
#     s = s.lower().replace(' ', '')
#     from string import ascii_lowercase
#     for i in range(len(ascii_lowercase)):
#         if ascii_lowercase[i] in s:
#             pass
#         else:
#             return False
#     return True
#
#
#     # return True if list(s) in list(ascii_lowercase) else False
#
# print(is_pangram("The quick brown fox jumps over the lazy dog"))
# print(is_pangram("Aacdefghijklmnopqrstuvwxyz"))
# print(is_pangram("The quick, brown fox jumps over the lazy dog!"))


# def in_array(array1: list, array2: list) ->list:
#     array3 = []
#     array2 = ' '.join(array2)
#     for i in range(len(array1)):
#         if array1[i] in array2 and array1[i] not in array3:
#             array3.append(array1[i])
#     # your code
#     return sorted(array3)
#
# print(in_array(['duplicates', 'duplicates'], ["lively", 'duplicates' "alive", "harp", "sharp", "armstrong"]))

# def count_smileys(arr:list[str]) -> int:
#     n = 0
#     for smile in arr:
#         smile = smile.replace('-', '')
#         smile = smile.replace('~', '')
#         if smile[0] == ':' or smile[0] == ';':
#             if smile[1] == ')' or smile[1] == 'D':
#                 n += 1
#     return n
    # ''.join(arr).count(')') + ''.join(arr).count('D')
    # return     ''.join(arr).count(')') + ''.join(arr).count('D')

# print(count_smileys([':D',':~)',';~D',':)']))    #the number of valid smiley faces in array/list
# print(count_smileys([':)',':(',':D',':O',':;']))    #the number of valid smiley faces in array/list
# print(count_smileys([';]', ':[', ';*', ':$', ';-D']))    #the number of valid smiley faces in array/list
# print(count_smileys([';]DD', ':[', ';*', ':$', ';-D']))    #the number of valid smiley faces in array/list
# def to_camel_case(text):
#     text = text.split('-')
#     rezalt = []
#     for i in text:
#         rezalt.append(i.capitalize())
#     text = ''.join(rezalt)
#     return text
#
# print(to_camel_case("the-stealth-warrior"))

# def to_camel_case(text):
#     text = text.replace('-', ' ')
#     text = text.replace('_', ' ')
#     text = text.split(' ')
#     rezult = text.pop(0)
#     for words in text:
#         words = words.title()
#         rezult += words
#     return rezult
#
# print(to_camel_case("the-stealth-warrior"))
# print(to_camel_case('The_stealth_warrior'))


def move_zeros(array: list) -> list:
    how_mach = array.count(0)
    for _ in range(how_mach + 1):
        try:
            array.remove(0)
            array.append(0)
        except:
            return array
    return array

print(move_zeros([1, 1, 2, 1, 3]))