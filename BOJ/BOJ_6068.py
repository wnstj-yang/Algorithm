# Baekjoon Online Judge - 6068번. 시간 관리하기

N = int(input())
time_list = []
for _ in range(N):
    T, S = map(int, input().split())
    time_list.append((T, S))
# 끝내야 하는 시간 기준으로 정렬
time_list.sort(key=lambda x: x[1])
result = 987654321
total = 0
for time, target in time_list:
    # 총 필요한 시간
    total += time
    # 필요한 시간이 제한 시간 보다 커지면 일을 못 끝낸다.
    if total > target:
        result = -1
        break
    # 제한 시간 - 현재까지 더한 총 필요한 시간을 적용해서 값이 최소인 것을 선택
    # 그러면 가장 늦은 시간에 일어날 수 있는 값을 구하기가 가능하다.
    result = min(result, target - total)
print(result)

