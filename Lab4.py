data = input("Введите строку: ").lower()
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя123456789"
analyze = {}

for i in range(0, len(data)):

    if data[i] in alphabet:
        if data[i] not in analyze.keys():
            analyze[data[i]] = 1
        else:
            count = analyze.get(data[i])
            analyze[data[i]] = count + 1

keys = list(analyze.keys())
buffer = ''

for i in range(0, len(keys) - 1):
    for j in range(i + 1, len(keys)):
        if analyze[keys[i]] < analyze[keys[j]]:
            buffer = keys[i]
            keys[i] = keys[j]
            keys[j] = buffer

for i in range(0, len(keys)):
    print(keys[i], ':', analyze[keys[i]])

"""
# вывод частот в алфавитном порядке
for i in range(0, len(alphabet)):
    if alphabet[i] in analyze.keys():
        print(alphabet[i], ':', analyze[alphabet[i]])
"""
