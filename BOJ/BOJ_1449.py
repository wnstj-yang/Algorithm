# Baekjoon Online Judge - 1449번. 수리공 항승
# 정공법? 으로 가야했다. 그리드는 언제나 어렵다...
# 오름차순 정렬 이후 문제의 조건에 맞게 조건식을 작성


N, L = map(int, input().split())
locations = list(map(int, input().split()))
locations.sort()
result = 1 
value = locations[0] - 0.5
for location in locations[1:]:
    if value + L >= location + 0.5:
        continue
    else:
        value = location - 0.5
        result += 1
print(result)
