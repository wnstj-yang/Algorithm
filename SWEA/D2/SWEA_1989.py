# SW Expert Academy - 1989번. 초심자의 회문 검사

T = int(input())

for tc in range(1, T + 1):
    string = input()
    left, right = 0, len(string) - 1
    check = True
    while left < right:
        if string[left] != string[right]:
            check = False
            break
        left += 1
        right -= 1
    if check:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))

