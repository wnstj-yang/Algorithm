# Baekjoon Online Judge - 15903번. 카드 합체 놀이

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
for _ in range(M):
    numbers.sort()
    num = numbers[0] + numbers[1]
    numbers[0], numbers[1] = num, num

print(sum(numbers))
