# 115~116p 실전 문제 - 왕실의 나이트

# 총 말이 움직이는 방향이 8방향
directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (-1, -2), (1, -2)]

info = input()
# 현재 위치를 x, y형태로 행열 구분
x = int(info[1])
y = int(ord(info[0]) - ord('a')) + 1

count = 0
for direction in directions:
    nx = x + direction[0]
    ny = y + direction[1]
    # 범위를 벗어난다면 말이 움직이지 못하므로 횟수 카운트 X
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    else:
        count += 1
print(count)
