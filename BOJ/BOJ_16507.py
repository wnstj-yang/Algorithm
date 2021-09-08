# Baekjoon Online Judge - 16507번. 어두운 건 무서워
# 그대로 풀면 시간초과 => 누적 합 이용


def prefix_sum():
    # (1,1) 이전의 경우 겹치는 부분이 없어 내비둔다
    for i in range(1, R+1):
        for j in range(1, C+1):
            img_info[i][j] = img_info[i][j-1] + img_info[i-1][j] - img_info[i-1][j-1] + img_info[i][j]


R, C, Q = map(int, input().split())
# (1,1) 이전의 경우에 인덱스 에러 방지를 위해 행과열 1줄씩 0 값을 추가해준다
img_info = [[0]*(C+1)] + [[0]+list(map(int, input().split())) for _ in range(R)]
prefix_sum()
for i in range(Q):
    # 좌표 정보 (r1, c1, r2, c2)
    r1, c1, r2, c2 = map(int, input().split())
    cnt = ((r2+1) - r1) * ((c2+1) - c1)
    ans = img_info[r2][c2] - img_info[r2][c1-1] - img_info[r1-1][c2] + img_info[r1-1][c1-1]
    print(ans // cnt)
