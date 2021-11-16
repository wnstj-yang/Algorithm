# Baekjoon Online Judge - 11931번. 수 정렬하기 4
# pypy3에서는 통과 / python3에서는 시간 초과
N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

numbers.sort(reverse=True)
for i in numbers:
    print(i)