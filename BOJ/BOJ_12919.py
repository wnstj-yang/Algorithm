# Baekjoon Online Judge - 12919번. A와 B 2


def check(string):
    # string의 문자열이 S와 같으면 1을 반환
    if string == S:
        return 1

    # 목표 문자열보다 길이가 낮거나 같은경우에는 0을 반환
    # 거꾸로 T에서 S로 가는 방향이기 떄문임.
    # 같은 것도 포함하는 이유는 같았어도 목표인 S와 다를 수 있어서이다
    if len(string) <= len(S):
        return 0
    # 전역변수 대신 따로 지역변수인 result을 선언해서 재귀로 받는다
    result = 0

    # 거꾸로이기 때문에 맨 뒤가 A이면 A를 지워준다
    if string[-1] == 'A':
        result = check(string[:-1])

    # 위의 재귀들을 거친 이후에 result가 1이면 1을 반환해준다
    if result == 1:
        return 1

    # 맨 앞이 B라면 역순으로 문자열을 뒤집은 이후에 마지막 B를 지운다
    if string[0] == 'B':
        temp = string[::-1]
        result = check(temp[:-1])
    # 조건들을 모두 진행한 이후의 결과값을 반환
    return result


# 입력받은 S를 T로 바꾸는 것이 문제이지만, T를 S로 만드는 방법으로 진행
S = list(input())
T = list(input())
print(check(T))
