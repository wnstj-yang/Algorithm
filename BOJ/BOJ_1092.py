# Baekjoon Online Judge - 1092번. 배

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
weights = list(map(int, input().split()))
# 크레인, 무게에 각각 내림차순 정렬
cranes.sort(reverse=True)
weights.sort(reverse=True)
result = 0
# 처음의 값이 크레인이 들 수 없는 무게라면 -1 출력
if weights[0] > cranes[0]:
    result = -1
else:
    # 이외의 경우 크레인의 수 만큼 들 수 무게들을 들 수 있는지 파악한다.
    while weights:
        for i in range(len(cranes)):
            for j in range(len(weights)):
                if weights[j] <= cranes[i]:
                    weights.pop(j)
                    break
        result += 1
print(result)
