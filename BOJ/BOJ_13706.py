# Baekjoon Online Judge - 13706번. 제곱근

N = int(input())
start = 0
end = N
while start <= end:
    mid = (start + end) // 2
    if mid ** 2 == N:
        print(mid)
        break
    # 중간 값의 제곱이 찾으려는 값보다 작으면 시작점을 중간 값 + 1
    if mid ** 2 < N:
        start = mid + 1
    # 중간 값의 제곱이 찾으려는 값보다 크면 끝 점을 중간 값 - 1
    else:
        end = mid - 1
