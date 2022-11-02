# text = input("вводи текст эксперементируй ")
text = "Мой дядя самых честных правил, когда не в шутку занемог..."
print("функция \"len\" - сколько символов len(text) = ", len(text))
input(">")
print("функция \"split\", преобразует текст в список text.split(\" \") = \n", text.split(" "))
input(">")
word = text.split(" ")
print("функция \"join\", список word (\" \").join(word) = ",(" ").join(word))
input(">")
print("функция \"join\", текст text (\"-\").join(text) = ", ("-").join(text))
search = input("ВНИМАНИЕ! Введи слово или символ, который будешь искать: ")
print('ищем совпадени в тексте text.find(search,[start],[end]. результат = ', text.find(search))
print('ищем совпадени в тексте text.rfind(search,[start],[end]. результат = ', text.rfind(search))


