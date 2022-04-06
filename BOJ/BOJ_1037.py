# Baekjoon Online Judge - 1037번. 약수

N = int(input())
# 해당 약수들을 나타내는 것임(1과 N제외). 그래서 최소 값과 최대 값을 곱해주면 약수들을 갖는 값을 찾기 가능
numbers = list(map(int, input().split()))
min_num = min(numbers)
max_num = max(numbers)
print(min_num * max_num)
