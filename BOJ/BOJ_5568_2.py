# Baekjoon Online Judge - 5568번. 카드 놓기

# 순열 구하는 라이브러리
from itertools import permutations

n = int(input())
k = int(input())
numbers = []
ans = set()
for _ in range(n):
    numbers.append(input())

# 모든 순열을 set에 넣어 중복 없이 구한다 
for i in permutations(numbers, k):
    ans.add(''.join(i))

# 개수를 구하는 것이니 길이를 구한다
print(len(ans))
