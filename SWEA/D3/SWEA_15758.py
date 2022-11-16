# SW Expert Academy - 15758번. 무한 문자열


# 유클리드 호제법 최대 공약수 구하기
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


T = int(input())

for tc in range(1, T + 1):
    s, t = map(str, input().split())
    len_s, len_t = len(s), len(t)
    check = False
    # 각 길이를 구해주고 최대공약수를 활용해 최소 공배수를 구한다.
    max_len, min_len = max(len_s, len_t), min(len_s, len_t)
    num = lcm(max_len, min_len)
    # 구한 최소 공배수(num)을 현재 입력받은 s와 t의 길이로 나눈 몫을 갖고 각각 똑같은 길이의 문자열로 만든다.
    s = s * (num // len_s)
    t = t * (num // len_t)
    # 서로 똑같은 길이의 문자열이 만들어지면 각각 비교해서 다른지 확인하여 무한반복할 필요 없이 결과값을 얻는다.
    for i in range(len(s)):
        if s[i] != t[i]:
            check = True
            break

    if check:
        print('#{} no'.format(tc))
    else:
        print('#{} yes'.format(tc))



