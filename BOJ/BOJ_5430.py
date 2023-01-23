# Baekjoon Online Judge - 5430번. AC

from collections import deque

T = int(input())

for _ in range(T):
    order = input()
    N = int(input())
    numbers = input()
    numbers = deque(numbers[1:-1].split(','))
    isReversed = False
    if numbers[0] == '':
        if 'D' in order:
            print('error')
        else:
            print('[]')
        continue
    check = True
    for o in order:
        if o == 'R':
            if isReversed:
                isReversed = False
            else:
                isReversed = True
        else:
            if numbers:
                if isReversed:
                    numbers.pop()
                else:
                    numbers.popleft()
            else:
                check = False
                break
    if check:
        if isReversed:
            numbers.reverse()
        numbers = '[' + ','.join(numbers) + ']'
        print(numbers)
    else:
        print('error')
