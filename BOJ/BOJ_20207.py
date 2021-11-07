# Baekjoon Online Judge - 20207번. 달력

# 각 일마다 일정이 몇개인지 count ( 1 ~ 365 )
work = [0] * 366

N = int(input())

for i in range(N):
    s, e = map(int, input().split())
    for j in range(s, e+1):
        work[j] += 1

width, height = 0, 0
ans = 0
for i in range(1, 366):
    # 0인 부분이라면 연결되지 않은 것 
    if work[i] == 0:
        # 가로 세로 값이 없으면 그냥 넘긴다.(어차피 연결된 것이 없음)
        if width == 0 and height == 0:
            continue
        else:
            # 연결된 것이 끝이라면 구했던 가로 세로를 곱하고 0으로 초기화 
            ans += width * height
            width, height = 0, 0
            continue
    else:
        # 0이 아니라면 연결될 수 있는 부분이기에 가로는 1씩 더하고 세로는 최대 값을 구한다
        width += 1
        height = max(height, work[i])
# 마지막에 구한 값을 더해주어야 끝남
ans += width * height
print(ans)
