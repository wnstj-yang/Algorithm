# Baekjoon Online Judge - 9375번. 패션왕 신해빈

T = int(input())
for _ in range(T):
    n = int(input())
    clothes = {}
    result = 1
    for _ in range(n):
        name, cloth = map(str, input().split())
        if cloth not in clothes:
            clothes[cloth] = [name]
        else:
            clothes[cloth].append(name)
    # 아무것도 입지 않은 것 까지 포함해서 + 1을 한 이후 각각 곱해줘서 경우의 수를 구한다. 
    for value in clothes.values():
        result *= len(value) + 1
    # 알몸인 상태를 제외해야 하므로 1을 빼준다
    print(result - 1)

