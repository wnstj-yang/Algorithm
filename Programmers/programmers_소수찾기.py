from itertools import permutations


def solution(numbers):
    answer = 0
    length = len(numbers)
    # 소수의 리스트를 set으로 선언하여 중복방지
    num_list = set()

    for i in range(1, length + 1):
        # i길이 만큼의 해당 numbers에서의 순열을 구한다
        # 튜플로 반환되기 때문에 list로 만들어준 이후
        perm_list = list(permutations(numbers, i))
        for perm in perm_list:
            # join함수를 사용한다( 리스트로 바꾸어야 한다. )
            perm = int(''.join(perm))
            if perm >= 2:
                check = True
                # 소수를 구할 때 루트 이용
                for i in range(2, int(perm ** 0.5) + 1):
                    if perm % i == 0:
                        check = False
                        break
                if check:
                    num_list.add(perm)

                    # 소수를 가지고 있는 num_list의 개수
    answer = len(num_list)
    return answer