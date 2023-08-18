alphabet = "#ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def finder(s1):
    for i in range(0, len(alphabet)):
        if s1 == alphabet[i]:
            return i


def encrypt(symbol, keypos, operation):
    if operation == 1:

        position = (finder(symbol) + finder(keypos)) % len(alphabet)
        return alphabet[position]

    elif operation == 2:

        position = (len(alphabet) + finder(symbol) - finder(keypos)) % len(alphabet)
        return alphabet[position]
