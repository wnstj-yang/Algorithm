# Baekjoon Online Judge - 1173번. 운동

N, m, M, T, R = map(int, input().split())

X = m
exercise, time = 0, 0
while exercise < N:
    # 맥박이 M을 넘어가면 운동 X이므로 끝
    if m + T > M:
        time = -1
        break
    # 운동 가능 경우
    if X + T <= M:
        X = X + T
        exercise += 1
    # 휴식 하는 경우
    else:
        X -= R
        if X < m:
            X = m
    time += 1
print(time)
