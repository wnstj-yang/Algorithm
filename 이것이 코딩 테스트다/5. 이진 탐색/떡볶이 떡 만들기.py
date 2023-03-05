# 이진 탐색 - 떡볶이 떡 만들기 - 201p


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

start = 0
end = max(numbers)
answer = 0
while start <= end:
    result = 0
    mid = (start + end) // 2
    for num in numbers:
        if num > mid:
            result += (num - mid)
    print(mid, result)
    if result < M:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid
print(answer)


# 4 6
# 19 15 10 17