# Baekjoon Online Judge - 20164번. 홀수 홀릭 호석


def getOdds(cal_result):
    odd = 0
    for i in str(cal_result):
        if int(i) % 2 == 1:
            odd += 1
    return odd


def check(num, result):
    global min_val, max_val
    # 길이가 1인 경우에는 최소, 최대값을 판단
    if len(num) == 1:
        min_val = min(min_val, result)
        max_val = max(max_val, result)
    # 길이가 2인 경우에는 각각의 숫자들을 더하고 나온 문자열을 바탕으로 홀수의 개수를 구하고,
    # 더해진 문자열로 재귀
    elif len(num) == 2:
        cal_result = str(int(num[0]) + int(num[1]))
        check(cal_result, result + getOdds(cal_result))
    else:
        # 3자리 이상이므로 범위를 벗어나지 않게 left 인덱스는 2를 빼주고
        # right인덱스는 총 길이에서 1을 빼준 상태까지를 리스트 슬라이싱을 진행한다
        # 2번째 반복문에서 적용 / a, b, c는 각 3개의 숫자 문자열을 나눈 이후의 값들을 말한다.
        for l in range(len(num) - 2):
            for r in range(l + 1, len(num) - 1):
                a = int(num[:l + 1])
                b = int(num[l + 1:r + 1])
                c = int(num[r + 1:])
                cal_result = str(a + b + c)
                check(cal_result, result + getOdds(cal_result))


N = input()
min_val = 987654321 # 최소값
max_val = 0 # 최대값
check(N, getOdds(N)) # 주어진 숫자 문자열 N과 첫 홀수의 개수
print(min_val, max_val)
