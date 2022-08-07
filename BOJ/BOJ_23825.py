# Baekjoon Online Judge - 23825번. SASA 모형을 만들어보자

N, M = map(int, input().split())
N = N // 2
M = M // 2
# 만드는데 2개씩 비용이 소모되기 때문에 그 중 최소 값을 구한다(SASA)
print(min(N, M))
