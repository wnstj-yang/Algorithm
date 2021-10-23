# Baekjoon Online Judge - 15654번. N과 M(5)

def check(idx):
    if idx == M:
        print(*ans)
        return

    for i in range(N):
        # 방문 체크를 통한 중복 수 방지
        if not visited[i]:
            visited[i] = True
            ans[idx] = numbers[i]
            check(idx+1)
            visited[i] = False


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
# 사전 순서 위해 정렬
numbers.sort()
visited = [0] * N
ans = [0] * M
check(0)
