# Baekjoon Online Judge - 10867번. 중복 빼고 정렬하기

N = int(input())
numbers = list(set(map(int, input().split())))
numbers.sort()
print(*numbers)
