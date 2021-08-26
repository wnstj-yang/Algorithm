# Baekjoon Online Judge - 9342번. 염색체
# 코드 간추리기

check_alpha = ['A', 'B', 'C', 'D', 'E', 'F']
T = int(input())

for i in range(T):
    chromosome = input()
    idx = 0
    check = True
    check_first = True
    length = len(chromosome)
    # 해당 문자열 있는지 파악
    for alpha in check_alpha:
        # 첫번째가 A이면 idx 추가 없음
        if alpha == 'A' and alpha == chromosome[idx]:
            break
        # 문자열에 속하는 것이 있다면 idx + 1
        if alpha == chromosome[idx]:
            idx += 1
            break
        # 없는 것이 있다면 답 X, check_first
        elif chromosome[idx] not in check_alpha:
            check_first = False

    if check_first:
        # 두 번째 규칙인 A가 계속 있는지 확인
        while True:
            # 인덱스 범위도 벗어나는지 확인
            if idx < length and chromosome[idx] == 'A':
                idx += 1
            else:
                break
        # 세 번째 규칙인 F가 계속 있는지 확인
        if chromosome[idx] == 'F':
            while True:
                if idx < length and chromosome[idx] == 'F':
                    idx += 1
                else:
                    break
        else:
            print('Good')
            check = False
        # 네 번째 규칙인 C가 계속 있는지 확인 (check로 이전 단계에서 규칙을 check)
        if check:
            if chromosome[idx] == 'C':
                while True:
                    if idx < length and chromosome[idx] == 'C':
                        idx += 1
                    else:
                        break
            else:
                print('Good')
                check = False
        # 마지막 규칙 체크
        if check:
            for alpha in check_alpha:
                if idx < length and alpha == chromosome[idx]:
                    idx += 1
                    break
            # 인덱스가 문자열의 길이보다 작으면 모든 규칙을 통과 X
            # 문자열의 길이보다 크면 인덱스 범위를 벗어난 것
            if idx != length:
                print('Good')
            else:
                print('Infected!')
    else:
        print('Good')

