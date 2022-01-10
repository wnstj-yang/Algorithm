# Baekjoon Online Judge - 11726번. 2xn 타일링

n = int(input())
numbers = [0] * 1001
numbers[1] = 1
numbers[2] = 2
# 각각 점화식을 세웠을 때 n이 3부터 1번, 2번째 이전의 값을 더한 값이 경우의 수를 나타내는 규칙이 존재한다
for i in range(3, n + 1):
    numbers[i] = numbers[i-1] + numbers[i-2]
print(numbers[n] % 10007)
