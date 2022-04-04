# Baekjoon online Judge - 1026번. 보물

N = int(input())
temp_A = list(map(int, input().split())) # 임시 A
B = list(map(int, input().split())) # 실제 B
A = [0] * N
temp_B = list(B) # 임시 B를 통해 가장 큰값의 위치를 구하면서 A의 가장 작은 값을 해당 위치에 놓는다.
for i in range(N):
    B_max_idx = temp_B.index(max(temp_B)) # B의 가장 큰 값의 인덱스
    A[B_max_idx] = min(temp_A) # B값이 가장 큰 곳에 A의 가장 작은 값을 놓는다.
    temp_A[temp_A.index(min(temp_A))] = 101 # 이후 A의 작은 값을 계속 구하기 위해 각 원소의 가장 큰 값으로 보이는 101로 초기화
    temp_B[B_max_idx] = -1 # 임시 B에 대해서 최대 값을 구하기 위해 -1로 초기화(0이 존재할 경우 방지)

# 즉, 그리디하게 고정된 B의 값에서 값이 큰 순서대로 A의 작은 값들로 채워넣어 곱한다.
result = 0
for i in range(N):
    result += (A[i] * B[i])
print(result)
