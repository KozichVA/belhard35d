# # 1. Написать функцию horse принимающая координаты (два числа в диапазоне от 0 до 8)
# # расположения коня на шахматной доске, вывести все позиции куда может перейти конь за 1
# # шаг
#
# # Функция для ввода значения, чтобы постоянно к ней возвращаться
# def start(coment = None):
#     if coment:
#         print(coment)
#     xy = list(input('Напишите позицию коня на шахмотной доске: ').lower().replace(' ', ''))
#     return xy
#
# # Проверяет адекватность ввода клетки доски
# def proverka():
#     xy = start()
#     x = str(xy[0])
#     y = str(xy[1])
#     if x.isdigit() or y.isalpha() or len(xy) > 2:
#         start('Ввели не верно, должно быть так: \"e3\".')
#     elif int(y) > 8:
#         start('Ввели не верно, на шахмотной доске 8 клеток')
#     # elif doska.get(x, False):
#         # start('Ввели не верно, нет такой буквы. Используйте: a, b, c, d, e, f, g, h')
#     else:
#         return x, int(y)
#
# def horse():
#     global doska
#     letter = []
#     i =[]
#     letter,i in doska.items()
#     x, y = proverka()
#     x = doska[x]
#     final_x = key[x - 3]
#     final_y = y + 1
#
# doska = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], (i for i in range(1, 9))))
# print(horse())
#
#
#
#
#
# # x - 2 y + 1
# # x + 2 y - 1
# # x + 1 y - 2
# # x - 1 y +2


# 2. «Ведьмаку заплатите чеканной монетой»
# Имеются монеты номиналом 1/5/10/25 копеек, написать функцию witcher, принимающая
# сумму в копейках, необходимо рассчитать сколько минимальное количество монет
# номиналом 1/5/10/25 необходимо чтобы составить данную сумму. Прим. 66 = 25 + 25 + 10 + 5
# + 1 ответ 5 монет
i25 = 0
i10 = 0
i5 = 0
i1 = 0
mony = int(input('перевод в монеты: '))
while mony != 0:
    if mony >= 25:
        mony = mony - 25
        i25 += 1
    elif mony >= 10:
        mony = mony - 10
        i10 += 1
    elif mony >= 5:
        mony = mony - 5
        i5 += 1
    elif mony >= 1:
        mony = mony - 1
        i1 += 1
print(f'''{i25} - монет по 25 копеек
{i10} - монет по 10 копеек
{i5} - монет по 5 копеек
{i1} - монет по 1 копейке''')



# 3. Написать функцию pow, которая принимает число А и число Б, необходимо с помощью
# рекурсии возвести число А в степень Б
def mulityplay(a,b,c = 1):
    c *= a
    b -= 1
    if b:
        return mulityplay(a, b, c)
    else:
        return c

print(mulityplay(int(input('введи А: ')), int(input('введи Б: '))))

# 4. Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё
# место в строю. Помогите ему это сделать. Программа получает на вход невозрастающую
# последовательность натуральных чисел, означающих рост каждого человека в строю. После
# этого вводится число X – рост Пети. Все числа во входных данных натуральные и не
# превышают 200.
# spisok = [192, 160, 149, 171, 120, 200, 180, 167, 153]
# petia = int((input('рост Пети: ')))
# spisok.append(petia)
# spisok.sort(reverse = True)
# print(spisok)
#
# for i in range(len(spisok)):
#     print(i)
#     if spisok[i] == petia and i == 0:
#         print('Петя, ты самый высокий')
#     elif spisok[i] == petia and i == len(spisok) - 1:
#         print('Иди в конец, Петя!')
#     elif spisok[i] == petia and petia != 200 and not i == 0:
#         print(f'Петя, становись между {i}-ым и {i + 2}-ым')
#     elif spisok.count(petia) > 1 and spisok[i] == petia:
#         print(f'Петя, становись перед {i}-ым, вы одного роста')

spisok = [192, 160, 149, 171, 120, 200, 180, 167, 153, 185]
petia = int((input('рост Пети: ')))
spisok.sort(reverse = True)
print(spisok)

for i in range(len(spisok)):
    if spisok[i] == petia and i == 0:
        print('Петя, ты самый высокий')
    elif petia < spisok[i] and i == len(spisok) - 1:
        print('Иди в конец, Петя!')
    elif spisok[i] > petia and spisok[i+1] < petia:
        print(f'Петя, становись между {i+1}-ым и {i + 2}-ым')
    elif spisok[i] == petia:
        print(f'Петя, становись перед {i+1}-ым, вы одного роста')
