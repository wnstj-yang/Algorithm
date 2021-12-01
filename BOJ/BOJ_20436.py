# Baekjoon Online Judge - 20436번. ZOAC 3

# 키보드 전체
keyboard = ['zxcvbnm', 'asdfghjkl', 'qwertyuiop']
# 모음
vowels = 'bnmhjklyuiop'

# 첫 시작점
s_l, s_r = map(str, input().split())
target = input()
ans = 0
# 왼쪽, 오른쪽 손가락의 위치
s_left, s_right = [], []
for i in range(3):
    if s_l in keyboard[i]:
        s_left = [i, keyboard[i].index(s_l)]
    if s_r in keyboard[i]:
        s_right = [i, keyboard[i].index(s_r)]

for alpha in target:
    # 모음에 존재한다면 오른쪽 손
    if alpha in vowels:
        for i in range(3):
            if alpha in keyboard[i]:
                pos = keyboard[i].index(alpha)
                dis = abs(s_right[0] - i) + abs(s_right[1] - pos) + 1
                ans += dis
                s_right[0], s_right[1] = i, pos
                break
    else:
        for i in range(3):
            # 자음 => 왼쪽 손가락
            if alpha in keyboard[i]:
                pos = keyboard[i].index(alpha)
                dis = abs(s_left[0] - i) + abs(s_left[1] - pos) + 1
                ans += dis
                s_left[0], s_left[1] = i, pos
                break
print(ans)
