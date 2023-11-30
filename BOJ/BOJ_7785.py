# Baekjoon Online Judge - 7785번. 회사에 있는 사람

N = int(input())
records = {}
for _ in range(N):
    name, status = map(str, input().split())
    if name not in records:
        records[name] = 1
    else:
        del records[name]
records = sorted(records.keys(), reverse=True)
for name in records:
    print(name)
