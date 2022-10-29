# Baekjoon Online Judge - 1946번. 신입 사원

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    info.sort()
    result = 1
    rank = info[0][1]
    # 서류심사 기준으로 오름차순정렬(순위이기때문), 면접결과로 판단을 하게 된다.
    # 여기서 다른 모든 지원자랑 비교를 해야되는데 사실 다른 어떤 지원자보다 순위가 낮은게 하나라도 있으면 어차피 안되기 때문에
    # 정렬된 상태에서 비교하면 된다.
    # 예를 들어 두 번째 테케에서 1, 4와 2, 5지원자랑 비교할 시 4가 5보다 작으므로 더 높다. 그러므로 2번째 지원자는 아예 떨어진다.
    for i in range(1, N):
        if info[i][1] < rank:
            result += 1
            rank = info[i][1]
    print(result)
