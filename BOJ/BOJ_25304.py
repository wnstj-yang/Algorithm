# Baekjoon Online Judge - 25304번. 영수증

X = int(input())
N = int(input())
result = 0
for _ in range(N):
    a, b = map(int, input().split())
    result += (a * b)
if result == X:
    print('Yes')
else:
    print('No')
