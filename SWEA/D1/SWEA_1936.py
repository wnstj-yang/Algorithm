# SW Expert Academy - 1936번. 1대1 가위바위보

A, B = map(int, input().split())

if A == 1:
    if B == 2:
        print('B')
    else:
        print('A')
elif A == 2:
    if B == 3:
        print('B')
    else:
        print('A')
else:
    if B == 1:
        print('B')
    else:
        print('A')