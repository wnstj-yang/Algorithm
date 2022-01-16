# Baekjoon Online Judge - 2015번. 수들의 합 4

N, K = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
result = {}
ans = 0
for i in range(len(numbers)-1):
    numbers[i+1] = numbers[i+1] + numbers[i]

for j in range(1, len(numbers)):
    if numbers[j] == K: # 1~j번째까지의 합이 K인경우
        ans += 1

    if numbers[j]-K not in result: # 인덱스 에러 방지
        result[numbers[j]-K] = 0
    # i~j번째 까지 K인 경우의 수를 구하면된다.
    # numbers[j] - numbers[i-1] = K 활용
    # 즉, j까지의 수 중 K인 개수를 딕셔너리에 저장
    ans += result[numbers[j]-K]
    # 각 부분합 수를 추가해준다
    if numbers[j] not in result:
        result[numbers[j]] = 1
    else:
        result[numbers[j]] += 1
print(ans)

