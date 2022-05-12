# Baekjoon Online Judge - 16208번 귀찮음

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
total = sum(numbers)
answer = 0
# 값이 큰 것과 총 길이에서 줄이면서 최소값을 저장해준다
for num in numbers:
    length = total - num
    answer += (num * length)
    total -= num
print(answer)

