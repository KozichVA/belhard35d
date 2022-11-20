# class User:
#
#     role: str = 'user'
#
#     def __init__(self, name: str, age: int) -> None:
#         self.age = age
#         self.first_name: str = name.title()
#         self.i = -1
#
#     def info(self) -> str:
#         return f'Name: {self.first_name} Role: {User.role}'
#
#     def __str__(self) -> str:
#         return f'Name: {self.first_name} Role: {User.role}'
#
#     def __int__(self) -> int:
#         return self.age
#
#     def __bool__(self) -> bool:
#         return self.role == 'user'
#
#     @classmethod
#     def change_role(cls, new_role: str) -> None:
#         cls.role = new_role.lower()
#
#     @staticmethod
#     def multiply(a: int, b: int) -> int:
#         return a * b
#
#     def __add__(self, other):
#         if isinstance(other, int):
#             self.age += other
#             return self.age
#         elif isinstance(other, User):
#             return self.age + other.age
#         else:
#             raise TypeError
#
#     def __radd__(self, other):
#         return self.__add__(other=other)
#
#     def __eq__(self, other) -> bool:
#         return self.age == other.age
#
#     def __ne__(self, other) -> bool:
#         return self.age != other.age
#
#     def __len__(self) -> int:
#         return self.age * 2
#
#     def __iter__(self) -> object:
#         return self
#
#     def __next__(self) -> str:
#         if self.i <= self.age:
#             self.i += 1
#             return str(self.i)
#         else:
#             raise StopIteration


# user1 = User(name='vasya', age=35)
# new_age = 2 + user1
# print(user1.age)
# user1.last_name = 'pupkin'
# print(user1.last_name)
# user2 = User(name='petya', age=24)
# print(user2 == user1)
# print(len(user1))
# user3 = User(name='masha')
# print(user1.info())
# print(user3.info())
# print(user2.last_name)
# User.change_role(new_role='admin')
# print(User.role)
# print(User.multiply(4, 5))
# for j in user1:
#     print(j)

# Написать класс Button, конструктор принимает обязательный атрибут text: str
# И не обязательный атрибут request_contact: bool (по умолчанию False)
# реализовать метод объекта dict() возвращающий словарь в формате
# {'text': self.text, 'request_contact': self.request_contact}

# Написать класс Keyboard, конструктор принимает атрибут keyboard - список списков экземпляров
# Button (обязательна проверка на структуру)
# написать метод serialize возвращающий разметку клавиатуры в виде списка списков словарей
# написать метод insert принимающий список классов Button и добавляющий этот список в атрибут keyboard в конец

#
# class Button:
#     """
#     Кнопка для клавиатуры
#     """
#
#     def __init__(self, text: str, request_contact: bool = False) -> None:
#         self.request_contact = request_contact
#         self.text = text
#
#     def dict(self) -> dict:
#         return {'text': self.text, 'request_contact': self.request_contact}


# class Keyboard:
#
#     def __init__(self, keyboard: list[list[Button]]) -> None:
#         if not isinstance(keyboard, list):
#             raise ValueError('argument `keyboard` must be list')
#         for line in keyboard:
#             if not isinstance(line, list):
#                 raise ValueError
#             for button in line:
#                 if not isinstance(button, Button):
#                     raise ValueError
#         self.keyboard = keyboard
#
#     def serialize(self) -> list[list[dict]]:
#         from copy import deepcopy
#         keyboard = deepcopy(self.keyboard)
#         for j in range(len(keyboard)):
#             for i in range(len(keyboard[j])):
#                 keyboard[j][i] = keyboard[j][i].dict()
#         return keyboard
#
#     def insert(self, keyboard: list[Button]):
#         if not isinstance(keyboard, list):
#             raise ValueError
#         for button in keyboard:
#             if not isinstance(button, Button):
#                 raise ValueError
#         self.keyboard.append(keyboard)
#
#
# buttons = [Button(text=text) for text in ('hello', 'python', 'world')]
# buttons = [[buttons[0], buttons[1]], [buttons[2]]]
# keyboard = Keyboard(keyboard=buttons)
# print(keyboard.serialize())


# def multiply(a: int, b: int) -> int:
#     """Произведение двух чисел
#
#     :param a: Первое число произведения
#     :param b: Второе число произведения
#     :return: Результат произведения
#     """
#     return a * b