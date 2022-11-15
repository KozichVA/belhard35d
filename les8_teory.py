# # # # # # # # # def decimal_to_binary(decimal):
# # # # # # # # #     binary = ''
# # # # # # # # #     while decimal > 0:
# # # # # # # # #         binary = str(decimal % 2) + binary
# # # # # # # # #         decimal //= 2
# # # # # # # # #     return binary
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # def binary_to_decimal(binary):
# # # # # # # # #     decimal = 0
# # # # # # # # #     for i in binary[::-1]:
# # # # # # # # #         decimal += int(i)
# # # # # # # # #         decimal *= 2
# # # # # # # # #     return decimal
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # def binary_to_decimal2(binary):
# # # # # # # # #     decimal = 0
# # # # # # # # #     binary = binary[::-1]
# # # # # # # # #     for i in range(len(binary)):
# # # # # # # # #         if binary[i] == '1':
# # # # # # # # #             decimal += 2 ** i
# # # # # # # # #     return decimal
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # print(binary_to_decimal2(binary=decimal_to_binary(decimal=18)))
# # # # # # # #
# # # # # # # #
# # # # # # # # morse = {
# # # # # # # #     'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•',
# # # # # # # #     'g': '——•', 'h': '••••', 'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
# # # # # # # #     'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•',
# # # # # # # #     's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
# # # # # # # #     'y': '—•——', 'z': '——••'}
# # # # # # # #
# # # # # # # #
# # # # # # # # def text_to_morse(text):
# # # # # # # #     global morse
# # # # # # # #     result = ''
# # # # # # # #     text = text.lower()
# # # # # # # #     for i in text:
# # # # # # # #         if i in morse:
# # # # # # # #             result += morse[i] + ' '
# # # # # # # #         elif i == ' ':
# # # # # # # #             result += '  '
# # # # # # # #     return result
# # # # # # # #
# # # # # # # #
# # # # # # # # def morse_to_text(morse_text):
# # # # # # # #     global morse
# # # # # # # #     morse_text = morse_text.replace('   ', ' | ').split()
# # # # # # # #     text = ''
# # # # # # # #     for i in morse_text:
# # # # # # # #         if i == '|':
# # # # # # # #             text += ' '
# # # # # # # #         else:
# # # # # # # #             for key, val in morse.items():
# # # # # # # #                 if i == val:
# # # # # # # #                     text += key
# # # # # # # #                     break
# # # # # # # #     return text
# # # # # # # #
# # # # # # # #
# # # # # # # # print(morse_to_text(text_to_morse(text='Hello world')))
# # # # # # #
# # # # # # #
# # # # # # # def list_offset(lst, n):
# # # # # # #     n -= len(lst) * (n // len(lst))
# # # # # # #     lst = lst[-n:] + lst[:-n]
# # # # # # #     return lst
# # # # # # #
# # # # # # #
# # # # # # # print(list_offset([1, 2, 3, 4, 5, 6, 7], -9))
# # # # # #
# # # # # #
# # # # # # lst = [2, 3, 4, 5, 'fghj', True, [], None, 'dfgh', 'fgh']
# # # # # # # var 1
# # # # # # # lst = list(filter(lambda x: isinstance(x, str), lst))
# # # # # # # print(lst)
# # # # # # # var 2
# # # # # # i = 0
# # # # # # while i < len(lst):
# # # # # #     if not isinstance(lst[i], str):
# # # # # #         del lst[i]
# # # # # #     else:
# # # # # #         i += 1
# # # # # # print(lst)
# # # # #
# # # # # numbers = [1, 2, 3, 4, 5, 6, 7]
# # # # #
# # # # #
# # # # # def my_reversed(lst):
# # # # #     for i in range(len(lst) // 2):
# # # # #         j = len(lst) - 1 - i  # индекс элемента с противоположной стороны
# # # # #         lst[i], lst[j] = lst[j], lst[i]
# # # # #         # lst[i], lst[~i] = lst[~i], lst[i]
# # # # #     return lst
# # # # #
# # # # #
# # # # # print(my_reversed(numbers))
# # # #
# # # # numbers = [2, 6, 3, 4, 3, 3, 5, 6, 8, 2, 34, 6, 4]
# # # #
# # # #
# # # # def my_sort(numbers):
# # # #     # result = []
# # # #     # for i in range(len(numbers)):
# # # #     #     if numbers[i] % 2:
# # # #     #         result.append(numbers[i])
# # # #     #     else:
# # # #     #         result.insert(0, numbers[i])
# # # #     # return result
# # # #     # for i in range(len(numbers)):
# # # #     #     if numbers[i] % 2 == 0:
# # # #     #         numbers.insert(0, numbers.pop(i))
# # # #     # return numbers
# # # #     numbers = list(filter(lambda x: not x % 2, numbers)) + list(filter(lambda x: x % 2, numbers))
# # # #     return numbers
# # # #
# # # #
# # # # print(my_sort(numbers))
# # #
# # #
# # # def sum_neighbor(numbers):
# # #     result = []
# # #     for i in range(len(numbers)):
# # #         if i < len(numbers) - 1:
# # #             result.append(numbers[i-1] + numbers[i+1])
# # #         else:
# # #             result.append(numbers[i-1] + numbers[0])
# # #     return result
# # #
# # #
# # # numbers = [1, 2, 3, 4, 5, 6, 7]
# # # print(sum_neighbor(numbers))
# # #
# #
# # countries = {
# #     'телемелитрямдия': ['нарния'],
# #     'россия': ['москва', 'питер'],
# #     'беларусь': ['минск', 'могилев', 'гомель']
# # }
# #
# #
# # def find_country(city):
# #     global countries
# #     for country, cities in countries.items():
# #         if city.lower() in cities:
# #             return country
# #     return 'страна не найдена'
# #
# #
# # print(find_country('могилев'))
#
#
# users = {
#     1: {
#         'name': 'alex',
#         'email': 'alex@gmail.com'
#     },
#     2: {
#         'name': 'pavel',
#         'email': ''
#     },
#     3: {
#         'name': 'masha'
#     }
# }
#
# for user in users.values():
#     # var 1
#     # if 'email' not in user:
#     #     print(user['name'])
#     # elif user['email'] == '':
#     #     print(user['name'])
#
#     # var2
#     if not user.get('email'):
#         print(user.get('name'))


# ______________________________________________________________________________________________________________
# Данна сумма вклада и процент по вкладу,
# сказать через сколько лет суммма вклада увеличиться в двое.
# (стафка рефинансирования)

# deposit = float(input('сумма вклада: '))
# n = float(input('процент: ')) / 100
# years = 0
# b = deposit * 2
# while deposit < b:
#     deposit *= (1 + n)
#     years += 1
# print(f'за {years} лет на вкладе будет {deposit.__round__()} $')

formula = input('введи формулу: ')
formula += '1' if formula.isalpha() else ''
print(formula)




