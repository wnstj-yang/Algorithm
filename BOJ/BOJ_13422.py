# Baekjoon Online Judge - 13422번. 도둑

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    houses = list(map(int, input().split()))
    answer = 0
    l, r = 0, M
    result = sum(houses[:M])
    # N과 M이 같을 때 체크 따로 필요
    if N == M:
        if result < K:
            answer += 1
    else:
        # l이 N까지 가면서 나머지 연산을 통해 r로 증가시키며 원형을 돌게끔 만든다.
        while l < N:
            if result < K:
                answer += 1
            result -= houses[l]
            result += houses[r % N]
            l += 1
            r += 1
    print(answer)
