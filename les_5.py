def calculate(k,m):
    znak = input('Введите "+", "-", "*", "/": ')
    if znak == '+':
        k += m
        print('Молодец, k+m= ', k)
    elif znak == '-':
        k -= m
        print('Молодец, k-m= ', k)
    elif znak == '*':
        k *= m
        print('Молодец, k*m= ', k)
    elif znak == '/':
        k /= m
        print('Молодец, k/m= ', k)
    else:
        print('Что-то не то ввел, а я не успокоюсь, пока ты не введёшь правильно: ')
        calculate(k,m)

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

print('Первые N цисел кратные M и больше K:')
multiplase = []
for n in range(n+1):
    if n % m == 0 and n > k:
        multiplase.append(n)

print('Все значения в одну строку:\n',multiplase)
conclusion = int(input('Сколько значений в строке выводить? '))

Multiplase = []
while len(multiplase):
    if len(multiplase) < conclusion:
        print(multiplase)
        break
    else:
        for i in range(conclusion) :
            Multiplase.append(multiplase.pop(0))
            Multiplase = sorted(Multiplase)
        print(Multiplase)
        Multiplase.clear()
print('\n\n')


    # Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число

print(f'Cделаем вычисления над числами k ={k} и m = {m}')
calculate(k,m)

# **Вывести четные числа от 2 до N по 5 в строку
print(f'\n\nВывести четные числа от 2 до N={n} по {conclusion} в строку')
input('>')
multiplase =[]
for n in range(n+1):
    if n == 0:
        pass
    elif not n % 2:
        multiplase.append(n)

how_many = len(multiplase) // conclusion
if len(multiplase) % conclusion:
    for i in range(how_many + 2):
        print(multiplase[conclusion*(i-1): conclusion * i])
else:
    for i in range(how_many + 1):
        print(multiplase[conclusion * (i - 1): conclusion * i])
