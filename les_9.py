class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False
        self.baby_seat = 'c детским креслом' if self.is_baby_seat else 'без детского кресла'

    def __str__(self):
        self.color = self.color.replace('ая', 'ого')
        return f'{self.count_passenger_seats}-х местная машинка {self.color.lower()} цвета {self.baby_seat}'


class Taxi(Car):
    def find_car(self, count_passengers: int, is_baby: bool) -> None:
        if count_passengers < self.count_passenger_seats and self.is_busy == False:
            if is_baby:
                return self if self.is_baby_seat else None
            else:
                return self
        else:
            return



car1 = Taxi('зеленая', 4, False)
car2 = Taxi('Красная', 6, True)
car3 = Taxi('Жёлтая', 2, False)
car4 = Taxi('Белая', 4, True)
car5 = Taxi('Чёрная', 4, True)
cars = [car1, car2, car3, car4, car5]

for car in cars:
    print(car.find_car(5, True))



