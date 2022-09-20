# SW Expert Academy - 1979번. 어디에 단어가 들어갈 수 있을까


T = int(input())

for tc in range(1, T + 1):
    result = 0
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 세로로 먼저 체크
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j]:
                cnt += 1
            else:
                # 검은색 부분 상태에서 K 개수라면 적합하므로 result + 1
                if cnt == K:
                    result += 1
                    cnt = 0
                # 이외는 0으로 다 초기화
                else:
                    cnt = 0
        if cnt == K:
            result += 1

    # 가로로 체크
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j]:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                    cnt = 0
                else:
                    cnt = 0
        if cnt == K:
            result += 1
    print('#{} {}'.format(tc, result))
