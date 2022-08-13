# Baekjoon Online Judge - 10162번. 전자레인지

T = int(input())
time = [300, 60, 10]
result = 0
if T % 10:
    print(-1)
else:
    for sec in time:
        if T >= sec:
            print(T // sec, end=' ')
            T = T % sec
        else:
            print(0, end=' ')
