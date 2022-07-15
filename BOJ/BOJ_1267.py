# Baekjoon Online Judge - 1267번. 핸드폰 요금

N = int(input())
call_time = list(map(int, input().split()))
m_cost, y_cost = 0, 0
#
for time in call_time:
    y_cost += 10 * (time // 30)
    if time % 30 + 1:
        y_cost += 10
    m_cost += 15 * (time // 60)
    if time % 60 + 1:
        m_cost += 15

if m_cost < y_cost:
    print('M {}'.format(m_cost))
elif m_cost == y_cost:
    print('Y M {}'.format(m_cost))
else:
    print('Y {}'.format(y_cost))
