# Заполнить список степенями числа 2 (от 2^1 до 2^n).
n = input("введите n: ")
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
