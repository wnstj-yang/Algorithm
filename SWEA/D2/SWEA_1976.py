# SW Expert Academy - 1976번. 시각 덧셈

T = int(input())

for tc in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    hour, minute = 0, 0
    minute = m1 + m2
    hour = h1 + h2
    if minute >= 60:
        minute -= 60
        hour += 1
    if hour > 12:
        hour -= 12
    print('#{} {} {}'.format(tc, hour, minute))
