# SW Expert Academy - 2029번. 몫과 나머지 출력하기

T = int(input())

for tc in range(1, T + 1):
    a, b = map(int, input().split())
    print('#{} {} {}'.format(tc, a // b, a % b))
