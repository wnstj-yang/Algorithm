# Baekjoon Online Judge - 25305번. 커트라인

N, k = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort(reverse=True)
print(scores[k - 1])
