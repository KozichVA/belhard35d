# Вывести первые N цисел кратные M и больше K
try:
    n = int(input('введите n :'))
    m = int(input('введите m :'))
    k = int(input('введите k :'))
except:
    print('ОШИБКА! Попробуйте ввести числа')
    n = int(input('введите n :'))
    m = int(input('введите m :'))
    k = int(input('введите k :'))

print('первые N цисел кратные M и больше K:')
multiplase = []
if n % m == 0 and n > k:
    multiplase.append(n)
while n :
    n -= 1
    if n % m == 0 and n > k:
        multiplase.append(n)
multiplase.reverse()

print('все значения в одну строку:\n',multiplase)
conclusion = 5
# int(input('сколько значений в строке выводить? '))

Multiplase = []
while len(multiplase):
    if len(multiplase) < conclusion:
        print(multiplase)
        break
    else:
        for i in range(conclusion) :
            Multiplase.append(multiplase.pop())
        print(Multiplase)
        Multiplase.clear()




    # Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число

# **Вывести четные числа от 2 до N по 5 в строку