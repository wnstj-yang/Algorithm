# Baekjoon Online Judge - 15665번. N과 M(11)

def check(idx):
    if idx == M:
        temp = tuple(ans)
        if temp not in duplicated:
            print(*ans)
        duplicated.add(temp)
        return
    # 중복 방지 + 중복 순열
    for i in range(N):
        ans[idx] = numbers[i]
        check(idx+1)


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [False] * N
duplicated = set()
ans = [0] * M
check(0)
