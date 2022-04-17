# 113~114p 예제 4 - 2, 시각

N = int(input())
result = 0
for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            # 3, 13 등 3이 하나라도 시각에 있는지 판단한다.
            if '3' in str(i) + str(j) + str(k):
                result += 1
print(result)
