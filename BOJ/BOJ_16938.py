# Baekjoon Online Judge - 16938번. 캠프 준비


def combi(idx, k, cnt):
    if k == cnt:
        candidates.append(list(temp))
        return
    for i in range(idx, len(numbers)):
        if not visited[i]:
            visited[i] = True
            temp[k] = numbers[i]
            combi(i, k + 1, cnt)
            visited[i] = False


# 조합으로 모든 경우의 수를 구하고 조건에 맞는 방법이 있으면 카운트
N, L, R, X = map(int, input().split())
numbers = list(map(int, input().split()))
candidates = []
result = 0
# 캠프에 사용할 문제는 2문제 이상임 / 2문제 이상부터 N개 까지의 조합을 모두 구한다.
for i in range(2, N + 1):
    temp = [0] * i
    visited = [False] * len(numbers)
    combi(0, 0, i)

# 구해진 조합들을 바탕으로 조건에 맞는 방법의 수를 카운팅
for candi in candidates:
    if L <= sum(candi) <= R and max(candi) - min(candi) >= X:
        result += 1
print(result)

