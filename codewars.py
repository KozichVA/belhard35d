# # # def bouncing_ball(h, bounce, window):
# # #     if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
# # #         return -1
# # #     n = 1
# # #     h *= bounce
# # #     while h > window:
# # #         h *= bounce
# # #         if h == window:
# # #             n += 1
# # #         n += 2
# # #
# # #     return n
# # #
# # # print(bouncing_ball(6, 0.5, 3))
# # def next_bigger(n):
# #     n = str(n)
# #     from itertools import permutations
# #     variant = list((permutations(n, len(n))))
# #     rezult = []
# #     for i in variant:
# #         rezult.append(''.join(i))
# #     rezult = set(rezult)
# #     rezult = sorted(rezult)
# #     try:
# #         return int(rezult[rezult.index(n) + 1])
# #     except:
# #         return -1
# #
# #
# #
# # def next_bigger(n):
# #     n = str(n)
# #     from itertools import permutations
# #     variant = list(permutations(n))
# #     rezult = []
# #     for i in variant:
# #         if int((''.join(i))) > int(n):
# #             rezult.append(int((''.join(i))))
# #     set(rezult)
# #     list(rezult)
# #     rezult = sorted(rezult)
# #     try:
# #         return rezult[0]
# #     except:
# #         return -1
# #
# # print(next_bigger(21238956123895618723))
#
#
#
# def score(dice: dict) -> int:
#     point = {1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200}
#     points = 0
#     from collections import Counter
#     check = Counter(dice)
#     for key, value in check.items():
#         if value >= 3:
#             points = point[key]
#             check[key] = value - 3
#             break
#     if check[1]:
#         points += 100 * check[1]
#     if check[5]:
#         points += 50 * check[5]
#     return points
#
#
# print(score([1, 1, 1, 1, 5]))
#
#
# def score(dice):
#     sum = 0
#     counter = [0, 0, 0, 0, 0, 0]
#     points = [1000, 200, 300, 400, 500, 600]
#     extra = [100, 0, 0, 0, 50, 0]
#     for die in dice:
#         counter[die - 1] += 1
#
#     for (i, count) in enumerate(counter):
#         sum += (points[i] if count >= 3 else 0) + extra[i] * (count % 3)
#
#     return sum
#
# print(score([1, 1, 1, 1, 5]))


# def increment_string(strng):
#     n = len(strng)
#     for i in range(n):
#         if strng[i].isdigit():
#             break
#     number = int(strng[i:]) + 1
#     return strng[0:i] + str(number)

# def increment_string(strng):
#     if len(strng) == 0:
#         return '1'
#     elif strng[-1].isalpha():
#         return strng + '1'
#     elif len(strng) == 1 and strng.isdigit():
#         return str(int(strng) + 1)
#     i = -1
#     while strng[i].isdigit():
#         i -= 1
#     number = int(strng[i+1:]) + 1
#     return  strng[0:1 + 1] + str(number).zfill(len(strng) - len(strng[i+1]))
#     # return strng[0:i + 1] + '0' * (len(strng[i+1:]) - len(str(number))) + str(number)

# print(increment_string('foobar23'))
# print(increment_string("foobar001"))
# print(increment_string("foo"))
# print(increment_string("foobar00"))
# print(increment_string('foobar23'))
# print(increment_string("foobar99"))
# print(increment_string("foobar099"))
# print(increment_string("fo99obar99"))
# print(increment_string(""))
# print(increment_string("asg09"))
# print(increment_string("asg0000009"))
# print(increment_string("v0"))
# print(increment_string("1"))

# def valid_parentheses(string):
#     string = list(filter(lambda x: not x.isalpha(), string))
#     string = ''.join(list(filter(lambda x: not x.isdigit(), string))).replace(' ','')
#     simbols = ['()', '[]', '{}', '<>']
#     for simbol in simbols:
#         while simbol in string:
#             string = string.replace(simbol, '')
#     #your code here
#     return bool(not string)
#
# print(f'{valid_parentheses("  (                ")} = False')
# print(f'{valid_parentheses(")test")} = False')
# print(f'{valid_parentheses("")} = True')
# print(f'{valid_parentheses("hi())(")} = False')
# print(f'{valid_parentheses("hi(hi)()")} = True')

# def valid_solution(board):
#     from itertools import permutations
#     var = permutations([*range(0, 10)], 9)
#     for gorizont in board:
#         if not gorizont in var:
#             return False
#         for i in range(0,10):
#             gorizont[i]
#     return

def valid_solution(board):
    for horizontal in board:
        if sum(horizontal) == 45 and len(set(horizontal)) == 9:
            print(f'горизонталь {sum(horizontal)}')
        else:
            return False
    Board = list(zip(*board))
    for vertical in Board:
        if sum(vertical) == 45 and len(set(vertical)) == 9:
            print(f'вертикаль {sum(vertical)}')
        else:
            return False
    return True

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                 [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                 [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                 [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                 [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                 [3, 4, 5, 2, 8, 6, 1, 7, 9]]))
print("Выше долждно быть True")
print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                 [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                 [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                 [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                 [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                 [3, 0, 0, 4, 8, 1, 1, 7, 9]]))
print("Выше долждно быть False")
print(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                                ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]))
print("Выше долждно быть True")
print(valid_solution(            [[1, 2, 3, 4, 5, 6, 7, 8, 9]
                                 ,[2, 3, 4, 5, 6, 7, 8, 9, 1]
                                 ,[3, 4, 5, 6, 7, 8, 9, 1, 2]
                                 ,[4, 5, 6, 7, 8, 9, 1, 2, 3]
                                 ,[5, 6, 7, 8, 9, 1, 2, 3, 4]
                                 ,[6, 7, 8, 9, 1, 2, 3, 4, 5]
                                 ,[7, 8, 9, 1, 2, 3, 4, 5, 6]
                                 ,[8, 9, 1, 2, 3, 4, 5, 6, 7]
                                 ,[9, 1, 2, 3, 4, 5, 6, 7, 8]]))

print("Выше долждно быть False")
print(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                                ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]))
print("Выше долждно быть False")





