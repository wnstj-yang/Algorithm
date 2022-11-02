# SW Expert Academy - 6485번. 삼성시의 버스 노선

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    bus_stop_numbers = [0] * 5001
    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            bus_stop_numbers[i] += 1
    P = int(input())
    print('#{} '.format(tc), end='')
    for _ in range(P):
        num = int(input())
        print(bus_stop_numbers[num], end=' ')
    print()
