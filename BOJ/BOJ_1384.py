# Baekjoon Online Judge - 1384번. 메시지


cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    check = False
    rel = []
    students = {}
    print('Group {}'.format(cnt))

    for i in range(N):
        info = list(map(str, input().split()))
        rel.append(info)

    for i in range(N):
        for j in range(1, N):
            # 규칙을 찾고 원형테이블에서 종이가 어떻게 오는지 찾아햐함
            if rel[i][j] == 'N':
                check = True
                if i - j < 0:
                    print('{} was nasty about {}'.format(rel[i - j + N][0], rel[i][0]))
                else:
                    print('{} was nasty about {}'.format(rel[i - j][0], rel[i][0]))
    if not check:
        print('Nobody was nasty')
    cnt += 1
    print()

