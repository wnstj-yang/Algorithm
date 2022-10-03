# SW Expert Academy - 11856번. 반반

T = int(input())

for tc in range(1, T + 1):
    word = input()
    alpha_list = {}
    for alpha in word:
        if alpha not in alpha_list:
            alpha_list[alpha] = 1
        else:
            alpha_list[alpha] += 1
    if len(alpha_list) == 2:
        check = True
        for value in alpha_list.values():
            if value != 2:
                check = False
                break
        if check:
            print('#{} Yes'.format(tc))
        else:
            print('#{} No'.format(tc))
    else:
        print('#{} No'.format(tc))
