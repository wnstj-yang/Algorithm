# Baekjoon Online Judge - 1233번. 주사위

S1, S2, S3 = map(int, input().split())
sum_list = {}
for i in range(1, S1 + 1):
    for j in range(1, S2 + 1):
        for k in range(1, S3 + 1):
            result = i + j + k
            if result not in sum_list:
                sum_list[result] = 1
            else:
                sum_list[result] += 1
# 딕셔너리로 값을 기준으로 내림차순 정렬(여러 개 인 경우 key값이 작은 것으로 출력해야 되는데 반영이 된다.)
sum_list = sorted(sum_list.items(), key=lambda x: x[1], reverse=True)
print(sum_list[0][0])
