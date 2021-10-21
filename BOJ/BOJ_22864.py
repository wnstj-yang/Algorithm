# Baekjoon Online Judge - 22864번. 피로도

A, B, C, M = map(int, input().split())
fatigability = 0
result = 0
# 하루 24시간동안
for i in range(24):
    # 우선적으로 피로도를 고려해서 넘으면 쉰다 (일을 최대한 하기 위함?)
    if fatigability + A > M:
        fatigability -= C
        if fatigability < 0:
            fatigability = 0
    else:
        result += B
        fatigability += A
print(result)