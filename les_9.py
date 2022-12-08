# class Car:
#     def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
#         self.color = color
#         self.count_passenger_seats = count_passenger_seats
#         self.is_baby_seat = is_baby_seat
#         self.is_busy = False
#         self.baby_seat = 'c детским креслом' if self.is_baby_seat else 'без детского кресла'
#
#     def __str__(self):
#         self.color = self.color.replace('ая', 'ого')
#         return f'{self.count_passenger_seats}-х местная машинка {self.color.lower()} цвета {self.baby_seat}'
#
#
# class Taxi(Car):
#     def find_car(self, count_passengers: int, is_baby: bool) -> None:
#         if count_passengers <= self.count_passenger_seats and self.is_busy == False:
#             if is_baby:
#                 self.is_busy = True
#                 return self if self.is_baby_seat else None
#             else:
#                 self.is_busy = True
#                 return self
#         else:
#             return
#
#
#
# car1 = Taxi('зеленая', 4, False)
# car2 = Taxi('Красная', 6, True)
# car3 = Taxi('Жёлтая', 2, False)
# car4 = Taxi('Белая', 4, True)
# car5 = Taxi('Чёрная', 4, True)
# cars = [car1, car2, car3, car4, car5]
#
# for car in cars:
#     print(car.find_car(2, False))


# 3. Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать ошибку
# ValueError
class Category():
    def __init__(self, categories: list[str]):
        self.categories = categories

    def add(self, categorie):
        if categorie in self.categories:
            raise ValueError(f'Такая категория уже существует под индексом: {self.categories.index(categorie)}')
        else:
            self.categories.append(categorie)
            return self.categories.index(categorie)
#
# # 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# # категорий на этом индексе, если нет элемента на таком индексе, вызвать атрибут ValueError
    def get(self, index):
        return self.categories[index] if index < len(self.categories) - 1 else 'ошибка!, не хочет в строку'
# # 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# # удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# # индексе, ничего не делать, метод ничего возвращать не должен
#
# # 3.4 Написать метод update принимающий индекс категорий и новое название категории, если
# # нет элемента на таком индексе, то новая категория должна добавляться с учетом того, что
# :имена категорий уникальны, если новое имя категории нарушает уникальность в списке
# # категорий, вызвать исключение ValueError
#
shop = Category(['фрукты', 'овощи', 'молочка'])
print(shop.add('канцтовары'))
# print(shop.add('овощи'))
print(shop.get(4))
print(shop.get(2))



# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool)
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение ValueError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение
# ValueError
