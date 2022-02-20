# Baekjoon Online Judge - 1992번. 쿼드트리


def check(x, y, div_num):
    flag = False
    cur_num = area[x][y] # 현재 값
    for i in range(x, x + div_num):
        for j in range(y, y + div_num):
            # 현재 값이랑 다를 경우 (0과 1이 다른 부분이 있을 시) 분할 => 압축가능 여부 판단
            if cur_num != area[i][j]:
                flag = True
                break
        if flag:
            break
    # flag를 통해 분할하면서 0과 1로 압축
    if flag:
        print('(', end='')
        div_num = div_num // 2
        check(x, y, div_num) # 왼쪽 위
        check(x, y + div_num, div_num) # 오른쪽 위
        check(x + div_num, y, div_num) # 왼쪽 아래
        check(x + div_num, y + div_num, div_num) # 오른쪽 아래
        print(')', end='')
    else:
        print(cur_num, end='')


N = int(input())
area = []
for _ in range(N):
    numbers = list(map(int, input()))
    area.append(numbers)
check(0, 0, N)
