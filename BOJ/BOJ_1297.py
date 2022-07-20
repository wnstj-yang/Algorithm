# Baekjoon Online Judge - 1297번. TV 크기

D, H, W = map(int, input().split())
# 비율이
# 실제 높이와 너비가 주어지는 대신 비율이 주어졌으므로 실제 값을 구하기 위해서는 (실제 값 / 비율)의 값을 가진 x를 구해야합니다.
# 피타고라스 공식과 실제 값 / 비율을 가진 x를 구한다
# c^2 = (ax)^2 + (bx)^2
x = (D / (H ** 2 + W ** 2) ** 0.5)
print(int(H * x), int(W * x))
