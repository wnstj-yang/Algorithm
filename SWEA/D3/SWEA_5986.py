# SW Expert Academy - 5986번. 새샘이와 세 소수


def is_prime():
    numbers = [False] * 1000
    for i in range(2, int(1000 * 0.5) + 1):
        if not numbers[i]:
            numbers[i] = False
            for j in range(i * i, 1000, i):
                if not numbers[j]:
                    numbers[j] = True
    temp = []
    for i in range(2, 1000):
        if not numbers[i]:
            temp.append(i)
    return temp


def search(num, cnt, idx):
    global result
    if cnt == 3:
        if num == N:
            result += 1
        return

    for i in range(idx, len(prime_numbers)):
        if num + prime_numbers[i] <= N:
            search(num + prime_numbers[i], cnt + 1, i)
        else:
            return


prime_numbers = is_prime()
length = len(prime_numbers)
T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    result = 0
    search(0, 0, 0)
    print('#{} {}'.format(tc, result))
