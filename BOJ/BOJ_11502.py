# Baekjoon Online Judge - 11502번. 세 개의 소수 문제


# 에라토스테네스의 체로 미리 소수 값들을 구한다
prime_candi = [True] * 1001 # 범위가 1000이기 때문에 크기 만큼 리스트 선언
# 제곱근까지 약수의 범위를 확인한다. 굳이 똑같은 것을 할 필요가 없기 때문
# Ex) 2 x 15해서 처리하나 15 x 2해서 처리하나 앞에서부터만 확인하면 된다
for i in range(2, int(1000 ** 0.5) + 1):
    if prime_candi[i]:
        # 순회하면서 False가 아닌 값들은 소수처리로 보고
        # 그 배수들은 False처리
        for j in range(i + i, 1001, i):
            prime_candi[j] = False
# 조건문을 줄이기 위해 소수들을 따로 빼놓는다
primes = [i for i in range(2, 1001) if prime_candi[i]]


T = int(input())
for _ in range(T):
    K = int(input())
    found = False # 답을 찾았는지 확인
    # 3중 포문을 돌면서 소수 3개가 찾아지는지 확인
    for i in primes:
        for j in primes:
            for k in primes:
                if i + j + k == K:
                    print(i, j, k)
                    found = True
                    break
            if found:
                break
        if found:
            break
    if not found:
        print(0)
