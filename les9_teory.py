# человек - класс
# Вадим - об ъект (экземпляр класса)
# рост - атрибут (условно переменные) общее значение, для всех объекта
# вырости, постареть - поведение

# Написать класс Button, конструктор принимает обязательный класс text: str
# И необязательный атрибут request_contact (False, по умолчанию)
# реализовать метод dict() возарщающий словарь в формате
# {'text': self.text, 'request_contact: self.request_contact'}
class Button:
    def __init__(self, text: str, request_contact: bool = False) -> None:
        self.request_contact =request_contact
        self.text = text
    def dict(self) -> dict:
        a = {'text': self.text, 'request_contact': self.request_contact}
        return a

a = Button.dict('asdf')
print(a)