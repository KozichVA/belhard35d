text = input("Введите слово: ")
text = text.replace(" ", "").lower()
index = len(text)
Littera = list(text)
print(f"Ваше слово состоит из {index} букв: {Littera}")

littera = []
i = 0
while i != index:
    for Letter in text[i]:
        i += 1
        littera.append(Letter)
print(f"Ваше слово состоит из {index} букв: {littera}")

russion_world = []
filename = "russian.txt"
for world in open(filename, 'r'):
    russion_world.append(world)

# print(russion_world[322])
# print("".join(littera))
# print(littera.join(" "))   !!!прикольная ошибка!!!