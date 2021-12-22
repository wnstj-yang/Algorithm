def check(x, y):
    if x > y:
        return x, y
    else:
        return y, x


def solution(n, m):
    answer = []
    # n, m중 큰 수 체크(x > y) - 유클리드 호제법
    x, y = check(n, m)
    # 최대공약수
    while y > 0:
        x, y = y, x % y
    answer.append(x)
    # 최소공배수 ( 주어진 두 수를 곱하고 최대공약수로 나눈다 )
    result = n * m // answer[0]
    answer.append(result)
    return answer
