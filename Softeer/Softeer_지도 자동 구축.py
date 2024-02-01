# 지도 자동 구축

N = int(input())
numbers = [0] * (N + 1)
numbers[0] = 2 # 첫 값은 2
# numbers[i] = (numbers[i - 1] + 2 ** (i - 1)) ** 2 => 식 / 편의상 제곱은 빼고 정답 출력 시 제곱 적용
for i in range(1, N + 1):
    numbers[i] = numbers[i - 1] + 2 ** (i - 1)
print(numbers[N] ** 2)
