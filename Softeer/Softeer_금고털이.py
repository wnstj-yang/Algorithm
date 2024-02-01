# 금고털이

W, N = map(int, input().split())
info = []
result = 0
for _ in range(N):
    m, p = map(int, input().split())
    info.append((m, p))
info.sort(key=lambda x:-x[1])
for m, p in info:
    # 0보다 크거나 작을 때면 더 이상 가격을 올릴 수 없다.
    if W <= 0:
        break
    # W가 i번째 금속의 무게인 m보다 크거나 같을 경우
    if W >= m:
        W -= m # 해당 m만큼 빼주고
        result += m * p # m * p만큼의 가격을 증가
    # W가 m보다 작은 경우
    else:
        result += W * p # 남은 무게인 W만큼 무게당 가격p를 곱해주고 더해준다
        W -= m # 계산의 편리를 위해 그냥 m을 빼준다
print(result)
