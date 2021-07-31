# Baekjoon Online Judge - 4659번. 비밀번호 발음하기
vowel = ['a', 'e', 'i', 'o', 'u']
while True:
    password = input()
    if password == 'end':
        break
    check = False
    # 1. 모음이 있는지 체크한다.
    cnt = 0
    for alpha in password:
        if alpha in vowel:
            # 존재하면 그 다음단계로 넘어간다. (check => True)
            # 모음이 존재하지 않으면 그 다음단계 진행 X
            check = True
            break

    if check:
        # 암호의 길이가 3개이상일 때 모음 혹은 자음이 3개 연속인지 확인한다.
        if len(password) >= 3:
            for i in range(1, len(password)-1):
                # 체크할 부분 ! => 한개의 모음 연속이 아닌 5개의 모음중 3개 연속으 의미한다. (자음도 포함)
                # 모음 3개 연속이면 그 다음단계 진행 X (check => False)
                if password[i-1] in vowel and password[i] in vowel and password[i+1] in vowel:
                    check = False
                    break
                # 자음 3개 연속이면 그 다음단계 진행 X (check => False)
                if password[i-1] not in vowel and password[i] not in vowel and password[i+1] not in vowel:
                    check = False
                    break
    if check:
        # 비밀번호 길이가 2개 이상이라면
        if len(password) >= 2:
            for i in range(len(password)-1):
                # 앞뒤가 같을 때
                if password[i] == password[i+1]:
                    # e 나 o 이면 pass
                    if password[i] == 'e' or password[i] == 'o':
                        continue
                    else:
                        check = False
                        break
    if check:
        print('<' + password + '> is acceptable.')
    else:
        print('<' + password + '> is not acceptable.')
