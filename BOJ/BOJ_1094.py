# Baekjoon Online Judge - 1094번. 막대기

X = int(input())
N = 64
result = 0
# X가 0이 될 때 까지(즉 X 길이만큼의 막대기들을 다 더하고 구해졌을 때까지) 아래의 과정
while X != 0:
    # N보다 X가 크거나 같다면 막대 길이에 더할 수 있는 것에 포함된다
    if X >= N:
        result += 1
        X -= N
    # 포함되지 않는 경우 절반씩 나눈다
    else:
        N //= 2
print(result)
