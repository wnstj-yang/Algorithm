# Programmers 소수 만들기

# 에라토스테네스의 체를 이용하여 소수를 구한다.
def get_prime():
    # 1000이하의 자연수 이고 3개일 때 최대는 3000까지를 구해야 하기 때문에 3001을 곱하낟.
    numbers = [True] * 3001

    for i in range(2, int(3001 ** 0.5) + 1):
        if numbers[i]:  # 소수인 경우
            for j in range(i + i, 3001, i):  # i의 배수들을 False
                numbers[j] = False
    return numbers


# 조합을 구한다.
def check(idx, t):
    global ans, numbers, answer, visited, isPrime
    if idx == 3:
        # 합이 소수인지 판단 맞으면 개수 카운트
        result = sum(ans)
        if isPrime[result]:
            answer += 1
        return
    for i in range(t, len(numbers)):
        if not visited[i]:
            visited[i] = True
            ans[idx] = numbers[i]
            check(idx + 1, i)
            visited[i] = False


def solution(nums):
    # global로 선언 후 다른 함수에서도 사용
    global ans, numbers, answer, visited, isPrime
    answer = 0
    visited = [False] * len(nums)
    numbers = nums
    ans = [0] * 3
    isPrime = get_prime()
    check(0, 0)

    return answer