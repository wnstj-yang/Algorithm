# Baekjoon Online Judge - 1461번. 도서관

# 각 left(음수), right(양수)부분들을 계산
def calcuate(arr):
    global result
    # 값이 남아있을 때까지 진행
    while arr:
        # 가장 큰 값까지 가서 왕복해서 오므로 가장 큰 값 * 2를 해주고 돌아오는 길에 M개 만큼 지운다
        num = arr[0]
        result += num * 2
        # 최대 M의 책을 가지고 이동하므로 M만큼의 개수를 지운다
        for _ in range(M):
            if len(arr) == 0:
                return
            arr.pop(0)


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
check = True
result = 0
# check가 참이면 음수에서 거리 상 큰 값이 있고, check 가 거짓이면 양수에서 거리 상 큰 값이 존재
if numbers[-1] > abs(numbers[0]):
    check = False
left = []
right = []
# left(음수), right(양수) 두 부분으로 나눈다
for num in numbers:
    if num < 0:
        left.append(abs(num))
    else:
        right.append(num)
# 둘 다 내림차순으로 정렬해서 맨 앞부터 뺴준다
left.sort(reverse=True)
right.sort(reverse=True)

# 각각 값이 존재하는지와 check값에 따라 제일 큰 값이 어디에 있는지 따져서 한 번만 큰 값을 저장해서 끝난다(왕복X)
if check and left:
    result += left[0]
    for _ in range(M):
        if len(left) == 0:
            break
        left.pop(0)
elif right:
    result += right[0]
    for _ in range(M):
        if len(right) == 0:
            break
        right.pop(0)

calcuate(left)
calcuate(right)
print(result)
