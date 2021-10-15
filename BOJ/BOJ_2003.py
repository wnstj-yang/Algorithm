# Baekjoon Online Judge - 2003번. 수들의 합 2
# 투포인터
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
e = 0
score = 0
cnt = 0
# s는 시작점을 의미
for s in range(N):
    # 점수가 목표보다 작고 e(끝 점)이 N보다 작아야한다
    while score < M and e < N:
        score += numbers[e]
        e += 1
    # 목표 점수랑 같다면 개수 cnt
    if score == M:
        cnt += 1
    # 위의 과정을 거친 이후면 s인 시작점이 달라져서 해당 위치 값을 빼준다
    score -= numbers[s]
print(cnt)