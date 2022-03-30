# Baekjoon Online Judge - 1182번. 부분수열의 합


def check(idx, cnt, target, result):
    global answer, S
    # 부분 집합 요소 개수만큼 구성을 했을 때
    if cnt == target:
        # 값이 같은 경우 갯수 증가
        if result == S:
            answer += 1
        return

    # 부분수열 구하는 부분(idx부터 인덱싱 설정)
    for i in range(idx, len(numbers)):
        check(i + 1, cnt + 1, target, result + numbers[i])


N, S = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0
# 부분집합을 구하는 요소의 개수
for i in range(1, N + 1):
    check(0, 0, i, 0)
print(answer)
