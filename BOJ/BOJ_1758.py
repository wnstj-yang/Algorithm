# Baekjoon Online Judge - 1758번. 알바생 강호

N = int(input())
tips = [] # 입력 받은 팁
answer = 0
for _ in range(N):
    tips.append(int(input()))
tips.sort(reverse=True)
# 팁이 높은 순서와 높은 등수라면 팁을 많이 받으므로 내림차순 정렬을 진행
for i in range(1, N + 1):
    result = tips[i - 1] - (i - 1) # 조건 맞게 계산. 0보다 크거나 작은 경우 팁 포함 X
    if result > 0:
        answer += result
print(answer)
