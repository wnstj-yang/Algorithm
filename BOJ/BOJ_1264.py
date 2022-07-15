# Baekjoon Online Judge - 1264번. 모음의 개수

while True:
    words = input().lower()
    if words == '#':
        break
    cnt = 0
    for alpha in words:
        if alpha in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
    print(cnt)
