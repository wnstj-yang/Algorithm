# Baekjoon Online Judge - 2839번. 설탕 배달
# 5 나머지 연산으로 최소의 개수를 위해 최대의 수로 나눈다 (그리디)
N = int(input())

cnt = 0
# N이 0보다 큰지 판별
while N > 0:
    # 5로 나누어 떨어지면 최소의 개수를 도달함
    if N % 5 == 0:
        cnt += N // 5
        break
    else:
        # 5로 나누어 떨어지지 않는다면 3을 빼고 개수 1 추가
        cnt += 1
        N -= 3
# N이 0보다 작다면 5와 3으로 나누어떨어지지 않는다는 의미
if N < 0:
    print(-1)
else:
    print(cnt)



