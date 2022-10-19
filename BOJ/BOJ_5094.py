# Baekjoon Online Judge - 5094번. Moo 게임

def func(now, k, N):
    # 주어진 점화식에 따라 매개변수에 있는 현재 길이인 now, 몇 번째인지 나타내는 k, 그리고 어느 위치에 있는 파악하기 위한 N
    prev = (now - k - 3) // 2 # 이전 길이의 수
    # 3등분으로 분할해서 나눴을 시 1번째 등분은 이전 길이까지 N을 비교 
    if N <= prev:
        return func(prev, k - 1, N)
    # 마지막 3번째 등분안에 N이 존재할 경우 이전의 길이에서 몇 번째 위치를 나타내는지 알려준다
    elif N > prev + k + 3:
        return func(prev, k - 1, N - prev - k - 3)
    # 가운데인 2번째 등분안에 존재한다면 'm' + 'o' * (k + 2)를 나타내므로 이 때는 바로 첫 번째가 아니라면 o를 반환
    else:
        if prev + 1 == N:
            return True
        else:
            return False

N = int(input())
length = 3
k = 0
# S(k) = 2 * S(k - 1) + k + 3으로 만들 수 있다.
# S(1) = 2 * S(0) + 'm' + 'o' * (1 + 2) <= 예시
# 그래서 구하려고 하는 N번째 위치만큼의 수 보다 큰 k값을 찾는다
while N > length:
    k += 1
    length = 2 * length + k + 3
if func(length, k, N):
    print('m')
else:
    print('o')
