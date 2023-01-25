# Baekjoon Online Judge - 1759번. 암호 만들기


def check(idx, k):
    if k == L:
        v_cnt = 0
        for v in vowel:
            v_cnt += temp.count(v)
        c_cnt = L - v_cnt
        if v_cnt >= 1 and c_cnt >= 2:
            candis.append(''.join(temp))
        return

    for i in range(idx, C):
        if not visited[i]:
            visited[i] = True
            temp[k] = alphabets[i]
            check(i, k + 1)
            visited[i] = False


L, C = map(int, input().split())
alphabets = list(map(str, input().split()))
alphabets.sort()
candis = []
temp = [''] * L
visited = [False] * C
vowel = ['a', 'e', 'i', 'o', 'u']
check(0, 0)
for i in candis:
    print(i)
