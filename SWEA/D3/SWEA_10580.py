# SW Expert Academy - 10580번. 전봇대

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lines = []
    cnt = 0
    for _ in range(N):
        x, y = map(int, input().split())
        # 각 선이 들어올 때 마다 대각선이 되는 부분에서 조건에 맞게 설정해서 맞으면 증가
        for lx, ly in lines:
            if x < lx and y > ly:
                cnt += 1
            elif x > lx and y < ly:
                cnt += 1
        lines.append((x, y))
    print('#{} {}'.format(tc, cnt))
