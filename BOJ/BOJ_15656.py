# Baekjoon Online Judge - 15656번. N과 M(7)

def check(k):
    if k == M:
        print(*ans)
        return
    # 중복허용
    for i in range(N):
        ans[k] = numbers[i]
        check(k+1)


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
ans = [0] * M
check(0)
