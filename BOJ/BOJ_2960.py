# Baekjoon Online Judge - 2960번. 에라토스테네스의 체


def check_prime():
    # 몇 번째인지 횟수 카운트
    cnt = 0
    # 원래는 int(N ** 0.5) + 1까지의 for문 범위르 잡아야하나
    # 소수를 구하려는 로직을 이용하되 몇 번째로 지워지는지 찾는 것이기
    # 때문에 N+1까지로 범위를 잡는다.
    for i in range(2, N+1):
        if numbers[i]:
            cnt += 1
            if cnt == K:
                return i
            for j in range(i + i, N+1, i):
                # 지워진 부분이라면 다음으로 넘어간다
                if numbers[j] == False:
                    continue
                cnt += 1
                if cnt == K:
                    return j
                numbers[j] = False


N, K = map(int, input().split())
numbers = [True] * (N + 1)
ans = check_prime()
print(ans)
