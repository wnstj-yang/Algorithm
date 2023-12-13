# Baekjoon Online Judge - 2605번. 줄 세우기

N = int(input())
arr = list(map(int, input().split()))
result = []
# 리스트를 순회하면서 인덱스 - 입력받은 값이 줄을 서야할 곳이므로 번호를 입력한다.
for i in range(N):
    result.insert(i - arr[i], i + 1)
print(*result)
