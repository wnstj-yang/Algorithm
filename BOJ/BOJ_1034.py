# Baekjoon Online Judge - 1034번. 램프


N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
K = int(input())
result = 0
# 행에 대한 0을 카운트해주면서 그에 따라 바꿀 수 있는 횟수가 되는지 판단.
# 1. 행의 0의 개수 <= K
# 2. 행의 0의 개수가 짝수면 K도 짝수, 홀수면 K도 홀수이여야 모두 바꾸기 가능하다
# 3. 조건에 맞다면 행을 탐색하면서 같은 친구들이 있는지 판단해서 최대 개수를 구한다

for i in range(N):
    zero_cnt = board[i].count(0)
    if zero_cnt <= K:
        if K % 2 == zero_cnt % 2:
            cnt = 0
            for j in range(N):
                if board[i] == board[j]:
                    cnt += 1
            result = max(result, cnt)
print(result)
