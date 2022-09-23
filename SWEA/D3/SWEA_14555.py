# SW Expert Academy - 14555번. 공과 잡초

# 문제 이해가 필요했던 것. 초원에 `놓았을 수 있는` 공의 개수의 최솟값의 의미
# ()인 경우 공이고, (l, l)처럼 잡초인 l에 가려져서 공일 수도 있지만 아닐 수도 있다는 의미이다.
# 그래서 이 경우도 공일 수 있는 것으로 생각한다.


T = int(input())

for tc in range(1, T + 1):
    grass = input()
    result = 0
    for i in range(len(grass) - 1):
        if grass[i] == '(' and grass[i + 1] == ')':
            result += 1
        elif grass[i] == '(' and grass[i + 1] == '|':
            result += 1
        elif grass[i] == '|' and grass[i + 1] == ')':
            result += 1
    print('#{} {}'.format(tc, result))
