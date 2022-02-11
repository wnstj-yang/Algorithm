# Baekjoon Online Judge - 9372번. 상근이의 여행

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
    # 사실 상 모든 국가가 연결되어 있기 때문에 N - 1출력하면 끝
    print(N - 1)
