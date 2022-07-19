# Baekjoon Online Judge - 1284번. 집 주소

numbers = {
    '0': 4, '1': 2, '2': 3
}

while True:
    N = input()
    if N == '0':
        break
    result = 0
    if len(N) > 1:
        result += len(N) - 1
    for num in N:
        if num not in numbers:
            result += 3
        else:
            result += numbers[num]
    result += 2
    print(result)
