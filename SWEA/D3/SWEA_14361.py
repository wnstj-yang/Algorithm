# SW Expert Academy - 14361번. 숫자가 같은 배수


def perm(k, length):
    if k == length:
        num = int(''.join(candi))
        if len(str(num)) == length:
            num_list.append(num)
        return

    for i in range(length):
        if not visited[i]:
            visited[i] = True
            candi[k] = N[i]
            perm(k + 1, length)
            visited[i] = False


T = int(input())

for tc in range(1, T + 1):
    N = list(map(str, input()))
    original = int(''.join(N))
    num_list = []
    length = len(N)
    candi = [0] * length
    visited = [False] * length
    perm(0, length)
    check = False
    # 순열을 활용해서 기존의 값과 다르고 기존의 값과 나머지 연산해서 0이 나오면 그 배수를 뜻한다.
    for num in num_list:
        if num != original and num % original == 0:
            check = True
            break
    if check:
        print('#{} possible'.format(tc))
    else:
        print('#{} impossible'.format(tc))

