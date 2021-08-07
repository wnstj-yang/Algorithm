# Baekjoon Online Judge - 2581번. 소수
#

M = int(input())
N = int(input())
ans = []
# numbers 1부터 10000까지 소수를 구한다
numbers = [True] * 10001
# M, N이 1이 주어졌을 때 소수가 아님을 방지
numbers[1] = False
# 에라토스테네스의 체 적용
for i in range(2, int(10000 ** 0.5) + 1):
    if numbers[i]:
        for j in range(i+i, 10001, i):
            if numbers[j] == False:
                continue
            numbers[j] = False

# ans리스트에 소수인 것들을 다 구한다.
for i in range(M, N+1):
    if numbers[i]:
        ans.append(i)
# 소수들의 합 및 최소값 / 소수존재하지 않으면 -1
if ans:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)
