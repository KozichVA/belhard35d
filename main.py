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
russion_world = []
filename = "russian.txt"
#Тут вообще чушь, но, слава богу, файл открылся.
for world in open(filename, 'r', encoding='utf-8'):
    russion_world.append(world)
#Тут есть ещё проблема с utf-8

print("ok, что-то ещё напишу... и!")
