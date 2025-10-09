spisok = input("Введите элементы списка через пробел: ")
chisla = spisok.split()
chisla = [int(x) for x in chisla]
dlina = len(chisla)
for i in range(dlina):
    for j in range(0, dlina - i - 1):
        if chisla[j] > chisla[j + 1]:
            chisla[j], chisla[j + 1] = chisla[j + 1], chisla[j]
print("Отсортированный список:", chisla)