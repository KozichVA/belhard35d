#Получаем список littera из букв слова введёного пользователем
text = input("Введите слово: ")
text = text.replace(" ", "").lower()
index = len(text)
littera = list(text)
print(f"Ваше слово состоит из {index} букв: {littera}")

#Получаем список russion_world из слов из файла со словами
russion_word = []
filename = "russian.txt"
for word in open(filename, 'r'):
        russion_word.append(word.replace("\n", ""))

#Сам не понимаю, что тут происходит
for num in range(len(russion_word)):
    letter = list(russion_word[num])

    proverka = []
    for i in range(len(letter)):
        proverka.append(letter[i] in littera)
    word_control = False in proverka

    if word_control == False:
        print(russion_word[num])
