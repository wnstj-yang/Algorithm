N, K = map(int, input().split())
country_info = []
rank = 1
ranks = {}
for _ in range(N):
    c, g, s, b = map(int, input().split())
    country_info.append([g, s, b, c])
country_info.sort(key=lambda x:(-x[0], -x[1], -x[2]))
prev = country_info[0][:3]
ranks[country_info[0][-1]] = rank
cnt = 0
for info in country_info[1:]:
    now, num = info[:3], info[-1]
    if prev != now:
        rank += (cnt + 1)
        cnt = 0
    else:
        cnt += 1
    ranks[num] = rank
    prev = now
print(ranks[K])
