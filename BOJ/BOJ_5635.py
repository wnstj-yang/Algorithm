# Baekjoon Online Judge - 5635번. 생일


N = int(input())
stu_info = {}
for _ in range(N):
    name, d, m, y = map(str, input().split())
    # 일 수와 월 수인 경우 길이가 1인 경우 그에 따른 문자열 '0'을 추가해준다
    if len(d) == 1:
        d = d + '0'
    if len(m) == 1:
        m = '0' + m
    # key, value로 keyt를 이름, value를 생일을 넣는다
    stu_info[name] = y + m + d
# 먼저 리스트로 만든 이후 생일을 기준으로 정렬을 진행한다
result = list(stu_info.items())
result.sort(key=lambda x: x[1])
# 첫번째는 최대값, 마지막은 최소값
print(result[-1][0])
print(result[0][0])
