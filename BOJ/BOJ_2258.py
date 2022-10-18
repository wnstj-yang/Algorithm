# Baekjoon Online Judge - 2258번. 정육점

N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
info.sort(key=lambda x:(x[1], -x[0]))
total = 0
result = 9999999999
same_price = 0
# 가격에 대한 오름차순과 무게에 대한 내림차순을 진행
for i in range(N):
    weight, price = info[i]
    # 가격이 같다면 그에 따른 예외처리 진행.
    # 가격의 오름차순정렬과 가격이 낮은 무게들을 더할 수 있기 때문에 같은 거라면 따로 처리해야함
    if i > 0 and price == info[i - 1][1]:
        same_price += price
    else:
        same_price = 0
    total += weight

    if total >= M:
        result = min(result, price + same_price)

if result == 9999999999:
    print(-1)
else:
    print(result)
