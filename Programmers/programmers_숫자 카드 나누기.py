# 유클리드 호제법 최대공약수(Greatest Common Divisor)
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(arrayA, arrayB):
    answer = 0
    max_A, max_B = arrayA[0], arrayB[0]
    a, b = True, True
    for a_num in arrayA[1:]:
        result_A = gcd(max(a_num, max_A), min(a_num, max_A))
        max_A = result_A

    for b_num in arrayB[1:]:
        result_B = gcd(max(b_num, max_B), min(b_num, max_B))
        max_B = result_B

    for i in range(len(arrayB)):
        if arrayB[i] % max_A == 0:
            a = False
        if arrayA[i] % max_B == 0:
            b = False
    if a:
        answer = max(answer, max_A)
    if b:
        answer = max(answer, max_B)

    return answer
