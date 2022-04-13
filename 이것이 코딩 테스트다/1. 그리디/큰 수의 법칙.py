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

# 수학으로 푸는 법 (M이 많이 커지면 시간 초과나기 때문)
# 반복되는 수열을 볼 수 있다. M // (K + 1)로 나눈 몫이 반복되는 수열이 나는 횟수. 여기에 K를 곱하면 가장 큰 수가 나오는 횟수
# 여기서 나누어 떨어지지 않을 수 있는데, 이는 M % (K + 1)만큼 나온 값을 더한다.
# 즉, count = M // (K + 1) * K 혹은 int(M / (K + 1)) * K
# count += M % (K + 1)
# 두 번째로 큰 수는 (M - count) * second를 진행

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