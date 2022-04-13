# 예제 3-1. 87p

N = int(input())
result = 0
coins = [500, 100, 50, 10]
# N은 10의 배수임
for coin in coins:
    q = N // coin
    result += q
    N %= coin
print(result)

# 입력
# 1260
