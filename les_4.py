# Заполнить список степенями числа 2 (от 2^1 до 2^n).
n = input("введите n (используется в 1-ом и 3-ем задании): ")
degree_two = []
for i in range(int(n)):
    degree_two.append(2 ** i)
print("Результат: ", degree_two)

# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры
text = list(input('Введите текст: ').replace(' ', ''))
text_control = list(text)
letter_control = {"Кол-во букв": "значение" }
for i in range(len(text_control)):
    num = text.count(text_control[i])
    letter_control[text_control[i]] = num

print(letter_control)

# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
print('\nПытка с заполнением адресной книги начинается...')
book = {'имя': 'почта'}
strange_book = {'номер': book}
for i in range(int(n)):
    name = input(f"Впишите имя {i}: ")
    email = input(f"Впишите e-mail {i}: ")
    book[name] = email
    strange_book[i] = book
print(strange_book)
