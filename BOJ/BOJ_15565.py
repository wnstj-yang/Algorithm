# Baekjoon Online Judge - 15565번. 귀여운 라이언

N, K = map(int, input().split())
arr = list(map(int, input().split()))
l, r = 0, 0
cnt = 0
if arr[r] == 1:
    cnt += 1
ans = 987654321
while r <= N - 1:
    # k개 라이언이면 최소 구간인지 체크 후 l(left) + 1
    if cnt == K:
        ans = min(ans, r - l + 1)
        if arr[l] == 1:
            cnt -= 1
        l += 1
    # K개 라이언이 아니면 r(right) + 1
    else:
        r += 1
        if r < N and arr[r] == 1:
            cnt += 1
# 위의 경우가 아니면 -1
if ans == 987654321:
    print(-1)
else:
    print(ans)
