# Baekjoon Online Judge - 1744번. 수 묶기


def calculate(arr):
    global max_result
    length = len(arr)
    # 홀수인 경우 마지막 값이 최소이고 이를 더해준다 
    if length % 2:
        for i in range(0, length - 1, 2):
            max_result += arr[i] * arr[i + 1]
        max_result += arr[-1]
    # 짝수인 경우 각각 곱해준 것을 더한다
    else:
        for i in range(0, length, 2):
            max_result += arr[i] * arr[i + 1]


N = int(input())
negative = []
positive = []
max_result = 0
for _ in range(N):
    num = int(input())
    # 규칙에 따라 1인 경우에는 더하는 것이 값을 올리므로 1을 기준으로 양수 음수 판단
    if num > 1:
        positive.append(num)
    elif num == 1:
        max_result += 1
    else:
        negative.append(num) # 0도 negative로 들어간다

# 양수는 내림차순, 음수는 오름차순으로 정렬
negative.sort()
positive.sort(reverse=True)

calculate(negative)
calculate(positive)
print(max_result)
