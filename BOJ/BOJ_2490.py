# Baekjoon Online Judge - 2490번. 윷놀이

for _ in range(3):
    info = list(map(int, input().split()))
    ans = [0, 0]
    for num in info:
        ans[num] += 1
    if ans[0] == 1:
        print('A')
    elif ans[0] == 2:
        print('B')
    elif ans[0] == 3:
        print('C')
    elif ans[0] == 4:
        print('D')
    else:
        print('E')
