# 정렬 - 유형별 문제. 국영수 359p
# https://www.acmicpc.net/problem/10825

N = int(input())
students = []
for _ in range(N):
    info = list(map(str, input().split()))
    students.append([info[0], int(info[1]), int(info[2]), int(info[3])])
students.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for info in students:
    print(info[0])
