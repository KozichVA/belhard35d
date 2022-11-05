# Заполнить список степенями числа 2 (от 2^1 до 2^n).
n = input("введите n: ")
degree_two = []
for i in range(int(n)):
    degree_two.append(2 ** i)
print("Результат: ", degree_two)

