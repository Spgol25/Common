n = int(input("Введите верхнюю границу поиска: "))

for i in range(2, n):
    s = 1
    for j in range(2, i):
        if i % j == 0:
            s += j
    if s == i:
        print(i)

