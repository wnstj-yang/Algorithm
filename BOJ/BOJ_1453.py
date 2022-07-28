# Baekjoon Online Judge - 1453번. 피시방 알바

N = int(input())
people = list(map(int, input().split()))
computers = [False] * 101
result = 0
for i in people:
    if not computers[i]:
        computers[i] = True
    else:
        result += 1
print(result)
