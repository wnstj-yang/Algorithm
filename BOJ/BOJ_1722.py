# Baekjoon Online Judge - 1722번. 순열의 순서


N = int(input())
info = list(map(int, input().split()))
perms = [0, 1]
# 순열에 대한 값들을 저장 
for i in range(2, 21):
    perms.append(perms[i - 1] * i)
numbers = [i for i in range(1, N + 1)] # 1 ~ N의 값들을 저장
# 소문제 1일 때
if info[0] == 1:
    k = info[1] - 1 # 인덱스 0부터 시작하므로 1을 빼준다
    result = []
    idx = N - 1 # 맨 앞에 순열 값에 0을 두어서 인덱스 상으로 표현
    # N - 1의 순열 값을 기준으로 k값을 나누어서 인덱스를 구해 위치를 알아놓는다.
    # 그 이후 numbers안에 있는 1 ~ N의 값을 제거하면서 마지막에는 하나 남은 것을 추가한다
    for _ in range(N - 1):
        num = k // perms[idx]
        result.append(numbers[num])
        numbers.remove(numbers[num])
        k = k % perms[idx]
        idx -= 1
    result.append(numbers[0])
    print(*result)

else:
    candi = info[1:]
    k = 0
    idx = N - 1
    for i in range(N - 1):
        # 주어진 N길이의 순열 값을 차례대로 인덱스에 순열값을 곱해주면서 위치를 찾는다
        k += numbers.index(candi[i]) * perms[idx]
        numbers.remove(candi[i])
        idx -= 1
    print(k + 1)
