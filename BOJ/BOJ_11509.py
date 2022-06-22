# Baekjoon Online Judge - 11509번. 풍선 맞추기

N = int(input())
numbers = list(map(int, input().split()))
result = 0
check = [0] * 1000001

for num in numbers:
    # 화살로 높이의 풍선에 맞았으므로 높이 1을 줄인 값에 화살의 수(위치) 증가
    if check[num] == 0:
        check[num - 1] += 1
        result += 1
    # 화살이 존재하는 경우 현재 화살 수를 줄이고 높이를 줄인 상태에서의 화살 수 증가
    else:
        check[num] -= 1
        check[num - 1] += 1
print(result)
