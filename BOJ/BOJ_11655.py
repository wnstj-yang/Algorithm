# Baekjoon Online Judge - 11655번. ROT13

string = input()
result = ''

for alpha in string:
    if alpha.isalpha():
        num = ord(alpha)
        if 65 <= num <= 90:
            result += chr((num - 65 + 13) % 26 + 65)
        elif 97 <= num <= 122:
            result += chr((num - 97 + 13) % 26 + 97)

    else:
        result += alpha
print(result)
