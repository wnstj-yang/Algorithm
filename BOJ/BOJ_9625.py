# Baekjoon Online Judge - 9625번. BABBA

K = int(input())
dp_A = [0] * 46
dp_B = [0] * 46
dp_A[0], dp_B[0] = 1, 0
dp_A[1], dp_B[1] = 0, 1
for i in range(2, K + 1):
    dp_A[i] = dp_A[i - 1] + dp_A[i - 2]
    dp_B[i] = dp_B[i - 1] + dp_B[i - 2]
print(dp_A[K], dp_B[K])
