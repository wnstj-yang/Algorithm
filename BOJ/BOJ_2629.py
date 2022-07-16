# Baekjoon Online Judge - 2629번. 양팔저울

def calculate(cnt, left, right):
    # 같은 단계에 있는 좌우 무게가 있다면 넘긴다.
    # 이와 같이 할 경우 왼쪽, 오른쪽 둘 다 똑같은 경우를 넘어간다.
    weight = abs(left - right)
    # 만들 수 있는 무게
    if weight not in w_list:
        w_list.append(weight)

    # cnt가 N개가 되면 return
    if cnt == N:
        return

    if dp[cnt][weight] == 0:
        calculate(cnt + 1, left + weights[cnt], right) # 왼쪽에 무게 추
        calculate(cnt + 1, left, right + weights[cnt]) # 오른쪽에 무게 추
        calculate(cnt + 1, left, right) # 무게 추 없이 진행
        dp[cnt][weight] = 1 # cnt번째 weight의 무게 추가 존재


N = int(input())
weights = list(map(int, input().split()))
M = int(input())
marbles = list(map(int, input().split()))
w_list = []
dp = [[0] * 15001 for _ in range(N + 1)]
calculate(0, 0, 0)

for i in marbles:
    if i in w_list:
        print('Y', end=' ')
    else:
        print('N', end=' ')
