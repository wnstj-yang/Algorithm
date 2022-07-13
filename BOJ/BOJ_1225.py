# Baekjoon Online Judge - 1225번. 이상한 곱셈

A, B = map(str, input().split())
result = 0
B_sum = sum(list(map(int, B)))
# 묶었을 경우 O(N^2)=> O(N)으로 가능
for i in A:
    result += (int(i) * B_sum)
print(result)
