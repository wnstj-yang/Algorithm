# Baekjoon Online Judge - 2525번. 오븐 시계

A, B = map(int, input().split())
C = int(input())
# 시로 된 것을 분으로 다 환산하여 진행
minute = A * 60 + B + C
hour = minute // 60
minute = minute % 60
if hour >= 24:
    hour -= 24
print(hour, minute)
