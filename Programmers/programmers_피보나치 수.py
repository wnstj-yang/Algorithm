def solution(n):
    # 재귀로 했을 시 시간초과이므로 10만개의 리스트로 값 저장
    fibo = [0] * 100001
    fibo[0], fibo[1] = 0, 1 # 초기값 저장
    # 피보나치 수 입력 (2부터 n까지)
    for i in range(2, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    return fibo[n] % 1234567


# 피보나치 수 리스트 추가방식
# def solution(n):
#     fibo = [0, 1, 1]
#     for i in range(3, n + 1):
#         fibo.append(fibo[i - 1] + fibo[i - 2])
#     answer = fibo[n] % 1234567
#     return answer
