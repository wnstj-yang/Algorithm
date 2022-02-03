# 유클리드 호제법 최대공약수 구하기
def gcd(x, y):
    if x < y:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x


def solution(w, h):
    # 전체 사각형 개수 = 총 개수 - ((길이 + 높이) - 최대공약수(길이, 높이))
    answer = w * h - (w + h - gcd(w, h))
    return answer
