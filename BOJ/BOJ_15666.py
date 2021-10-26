# Baekjoon Online Judge - 15666번. N과 M(12)

def check(k, idx):
    if idx == M:
        temp = tuple(ans)
        if temp not in duplicated:
            print(*ans)
        duplicated.add(temp)
        return
    # 중복 방지 + 중복 조합
    for i in range(k, N):
        ans[idx] = numbers[i]
        check(i, idx+1)


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
duplicated = set()
ans = [0] * M
check(0, 0)

