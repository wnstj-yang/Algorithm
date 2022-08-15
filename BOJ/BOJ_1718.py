# Baekjoon Online Judge - 1718번. 암호

plain = input()
encrypt = input()
result = ''
for i in range(len(plain)):
    if plain[i].isalpha():
        e = ord(encrypt[i % len(encrypt)])
        value = (ord(plain[i]) - e - 1) % 26
        result += chr(value + 97)
    else:
        result += plain[i]
print(result)
