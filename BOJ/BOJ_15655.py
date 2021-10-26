# Baekjoon Online Judge - 15655번. N과 M(6)

def check(k, idx):
    if k == M:
        print(*ans)
        return
    # k가 갯수, idx로 조합을 구하기 위해 인덱스설정
    for i in range(idx, N):
        ans[k] = numbers[i]
        check(k+1, i+1)


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
# 오름차순 위해 정렬
numbers.sort()
ans = [0] * M
check(0, 0)
