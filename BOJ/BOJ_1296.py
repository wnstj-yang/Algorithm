# Baekjoon Online Judge - 1296번. 팀 이름 정하기

yd = input()
N = int(input())
result = []
count_love = {
    'L': 0, 'O': 0, 'V': 0, 'E': 0
}
for alpha in yd:
    if alpha in count_love:
        count_love[alpha] += 1

for _ in range(N):
    name = input()
    count_temp = dict(count_love)

    for alpha in name:
        if alpha in count_temp:
            count_temp[alpha] += 1
    L, O, V, E = count_temp['L'], count_temp['O'], count_temp['V'], count_temp['E']
    prob = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    result.append([prob, name])

# 확률값은 내림차순, 이름은 오름차순으로 정렬
result.sort(key=lambda x: (-x[0], x[1]))
print(result[0][1])
