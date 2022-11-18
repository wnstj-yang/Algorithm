# SW Expert Academy - 5688번. 세제곱근을 찾아라
# 아래 방법 외에도 N ** 1/3을 해줘서 주어지는 값에 따라 정수 값 혹은 -1을 출력하는 것도 있다.

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    answer = -1
    for i in range(1, 10 ** 6 + 1):
        if i * i * i == N:
            answer = i
            break
    print('#{} {}'.format(tc, answer))
