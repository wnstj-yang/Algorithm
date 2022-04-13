# 92p 실전 문제 - 큰 수의 법칙

N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
first, second = numbers[0], numbers[1]
result = 0
cnt = 0
# 첫 번째, 두 번째 큰 값들로 가장 큰 값은 K번, 두 번째로 큰 값은 1번 더해주고 다시 가장 큰 값으로 K번 반복
for _ in range(M):
    # K번 더했다면 두번째를 더해주고 횟수 초기화
    if cnt == K:
        cnt = 0
        result += second
        continue
    result += first
    cnt += 1
print(result)

# 입력 - 1
# 5 8 3
# 2 4 5 4 6

# 출력 - 1
# 46

# 입력 - 2
# 5 7 2
# 3 4 3 4 3

# 출력 - 2
# 28