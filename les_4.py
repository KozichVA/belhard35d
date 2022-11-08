# Заполнить список степенями числа 2 (от 2^1 до 2^n).
n = input("введите n (используется в 1-ом и 3-ем задании): ")
degree_two = []
for i in range(int(n+1)):
    degree_two.append(2 ** (i))
print("Результат: ", degree_two)

# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры
text = list(input('Введите текст: ').replace(' ', ''))
text_control = list(text)
letter_control = {"буква": "количество"}
for i in range(len(text_control)):
    num = text.count(text_control[i])
    letter_control[text_control[i]] = num

print(letter_control)

# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

print('\nПытка с заполнением адресной книги начинается...')
book = {'имя': 'e-mail'}
strange_book = {'номер': {'имя': 'e-mail'}}
for i in range(int(n)):
    name = input(f"Впишите имя {i + 1}: ")
    email = input(f"Впишите e-mail {i + 1}: ")
    book[name] = email
    strange_book[i] = book.copy()
    book.clear()
print(strange_book)
print(strange_book['номер'])

# print('\nПытка с заполнением адресной книги начинается...')
# Name =[]
# Email = []
# strange_book = {'номер': 'словарь'}
# for i in range(int(n)):
#     name = input(f"Впишите имя {i + 1}: ")
#     email = input(f"Впишите e-mail {i + 1}: ")
#     Name.append(name)
#     Email.append(email)
#     strange_book[i] = dict(zip(Name, Email))
#     Name.clear()
#     Email.clear()
# print(strange_book)