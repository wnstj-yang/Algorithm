# Baekjoon Online Judge - 10825번. 국영수

N = int(input())

scores = []
for _ in range(N):
    info = list(map(str, input().split()))
    for i in range(1, 4):
        info[i] = int(info[i])
    scores.append(info)

scores.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
ans = []
for i in range(N):
    print(scores[i][0])
