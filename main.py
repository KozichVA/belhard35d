text = input("Введите слово: ")
text = text.replace(" ","").lower()
index = len(text)
littera = []
i = 0
while i != index:
    for Letter in text[i]:
        i += 1
        littera.append(Letter)

print(littera)