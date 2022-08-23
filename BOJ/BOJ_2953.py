# Baekjoon Online Judge - 2953번. 나는 요리사다

arr = [list(map(int, input().split())) for _ in range(5)]
num = 0
result = 0
for i in range(5):
    if sum(arr[i]) > result:
        num = i + 1
        result = sum(arr[i])
print(num, result)
