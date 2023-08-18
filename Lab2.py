from encryption import encrypt as enc

alphabet = "#ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""
k = 0


stin = input("Введите строку: ").upper()
key = input("Введите ключ: ").upper()

while len(key) < len(stin):
    key += key[k]
    k += 1

operation = int(input("Выберите действие:\n 1.Шифрование.\n 2.Дешифрование.\n"))

if operation == 1:

    for j in range(0, len(stin)):
        result += enc(stin[j], key[j], operation)

elif operation == 2:

    for j in range(0, len(stin)):
        result += enc(stin[j], key[j], operation)

print("Результат шифрования:", result)

