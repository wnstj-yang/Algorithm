# SW Expert Academy - 1948번. 날짜 계산기

T = int(input())
days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
for tc in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    result = 0
    for i in range(m1, m2):
        if i == m1:
            result += days[i] - d1 + 1 # 당일위해 1
        else:
            result += days[i]
    result += d2
    print('#{} {}'.format(tc, result))

