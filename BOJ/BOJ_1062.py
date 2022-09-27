# Baekjoon Online Judge - 1062번. 가르침


def search(idx, cnt):
    global result
    if cnt == K - 5:
        w_cnt = 0
        for word in words:
            check = True
            for alpha in word:
                if not visited[ord(alpha) - 97]:
                    check = False
                    break
            if check:
                w_cnt += 1
        result = max(result, w_cnt)
        return

    for i in range(idx, 26):
        if not visited[i]:
            visited[i] = 1
            search(i, cnt + 1)
            visited[i] = 0


N, K = map(int, input().split())
words = set()
visited = [0] * 26
result = 0
for _ in range(N):
    words.add(input())

for alpha in ['a', 'n', 't', 'i', 'c']:
    visited[ord(alpha) - 97] = 1

if K >= 5:
    if K == 26:
        print(len(words))
    else:
        search(0, 0)
        print(result)

else:
    print(0)