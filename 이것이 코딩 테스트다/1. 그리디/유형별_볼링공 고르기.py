# 유형별 문제 5. 볼링골 고르기 - 315p

# 그리디하게 푸는 방법
# 조합형태여도 서로 다른 수로 인식한다. 2가 2개있고 3도 2개있을 때 (2, 3)이 2번나온다. 즉, 수가 같다고 같은 주소값이 아니라고 생각
# 그래서 N -= 각 수의 개수 * N
# 즉, 조합을 그리디하게 푼다와 같이 보면 될 것 같다.
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
nums_cnt = [0] * 11
result = 0
for num in numbers:
    nums_cnt[num] += 1

# 각 수의 개수에서 남은 숫자들의 개수를 곱하는 방식으로 경우의 수를 구한다.
for i in range(1, M + 1):
    N -= nums_cnt[i]
    result += (N * nums_cnt[i])
print(result)


# 기존 형태로 서로 다른 2개를 고르는 조합 방법
# N, M = map(int, input().split())
# balls = list(map(int, input().split()))
# result = 0
# for i in range(len(balls) - 1):
#     for j in range(i + 1, len(balls)):
#         if balls[i] != balls[j]:
#             result += 1
# print(result)


# 입력 - 1
# 5 3
# 1 3 2 3 2
# 출력 - 1
# 8


# 입력 - 2
# 8 5
# 1 5 4 3 2 4 5 2
# 출력 - 2
# 25
