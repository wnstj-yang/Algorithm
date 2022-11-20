# SW Expert Academy - 5549번. 홀수일까 짝수일까

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    if N % 2:
        print('#{} Odd'.format(tc))
    else:
        print('#{} Even'.format(tc))
