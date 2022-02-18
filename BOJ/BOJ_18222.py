# Baekjoon Online Judge - 18222번. 투에-모스 문자열
# 투에모스 문자열 그냥 재귀로 하면 시간초과 => 점화식 활용
# t0 = 0, t2n = tn, t2n+1 = 1 - tn (짝홀 구분)

def recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # 0, 1 제외 홀수
    elif n % 2:
        return 1 - recursive(n // 2)
    else:
        return recursive(n // 2)


k = int(input())
print(recursive(k - 1))
