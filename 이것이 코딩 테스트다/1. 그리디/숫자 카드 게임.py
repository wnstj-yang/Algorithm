# 96p 실전문제 - 숫자 카드 게임

result = 0
N, M = map(int, input().split())

for _ in range(N):
    cards = list(map(int, input().split()))
    min_value = min(cards) # 행에서 최소 값
    result = max(result, min_value) # 각 행을 돌면서 최대 값을 구한다.
print(result)

# 입력 - 1
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2
# 출력 - 1
# 2

# 입력 - 2
# 2 4
# 7 3 1 8
# 3 3 3 4
# 출력 - 2
# 3
