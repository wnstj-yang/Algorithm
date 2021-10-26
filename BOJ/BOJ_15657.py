# Baekjoon Online Judge - 15657번. N과 M(8)


def check(k, idx):
    if k == M:
        print(*ans)
        return
    # 중복허용하나 비내림차순이여야함
    for i in range(idx, N):
        ans[k] = numbers[i]
        check(k+1, i)


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
ans = [0] * M
check(0, 0)
