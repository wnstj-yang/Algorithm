def isPrime(N):
    m = int(N ** 0.5) + 1
    if N == 1:
        return False
    for i in range(2, m):
        if N % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    # 1. 10진수를 k진수로 변환하기
    result = ''
    while n >= k:
        num = n % k
        result = str(num) + result
        n = n // k
    result = str(n) + result  # 마지막 값 추가
    # 2. 조건에 따라 소수인 수인지 판단
    prime_num = ''
    for idx in range(len(result)):
        if result[idx] != '0':
            prime_num += result[idx]
        else:
            # 0이지만 비어있다면 pass
            if prime_num == '':
                continue
            # 소수판별을 진행해서 소수라면
            if isPrime(int(prime_num)):
                answer += 1
            prime_num = ''  # 빈 문자열로 초기화
    # 마지막까지 비어있지 않은 수에 대한 소수 판별 진행
    if prime_num != '':
        if isPrime(int(prime_num)):
            answer += 1
    return answer
