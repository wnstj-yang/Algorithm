# SW Expert Academy - 9480번. 민정이와 광직이의 알파벳 공부
alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def comb(idx, k, length):
    global result
    if k == length:
        # 알파벳 검사
        cnt = 0
        string = ''.join(candi)
        # 런타임 에러가 나지 않게 위의 딕셔너리의 알파벳들을 체크한다.
        # 기존에 cnt = [1] * 26으로 했을 때 스택 메모리 초과로 생각이 되어진다.
        for alpha in alphabets:
            if alpha in string:
                cnt += 1
        if cnt == 26:
            result += 1

        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            candi.append(words[i])
            comb(i, k + 1, length)
            visited[i] = False
            candi.pop()


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    words = []
    result = 0
    for _ in range(N):
        words.append(input())

    for i in range(1, N + 1):
        visited = [False] * N
        candi = []
        comb(0, 0, i)
    print('#{} {}'.format(tc, result))
