# Baekjoon Online Judge - 9655번. 돌 게임

N = int(input())
cnt = 0
while N > 0:
    # 돌을 1개 또는 3개 가져갈 수 있으므로 3개이상이면 3개를 뺴주고 횟수 카운트
    if N >= 3:
       N -= 3
       cnt += 1
    # 3개 미만이면 1씩 차감
    else:
        N -= 1
        cnt += 1
# 횟수를 카운트해서 홀수이면 상근이가 이기고, 짝수이면 창영이가 이긴다.
if cnt % 2:
    print("SK")
else:
    print("CY")
