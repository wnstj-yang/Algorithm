# Baekjoon Online Judge - 19639번. 배틀로얄

X, Y, M = map(int, input().split())
enemy = [int(input()) for _ in range(X)]
heal = [int(input()) for _ in range(Y)]


e_idx, h_idx = 0, 0
now = M
ans = []
for _ in range(X + Y):

    if now > M // 2 and e_idx < X:
        now -= enemy[e_idx]
        e_idx += 1
        ans.append(-e_idx)

    if now <= M // 2 and h_idx < Y:
        now += heal[h_idx]
        h_idx += 1
        ans.append(h_idx)

    if e_idx == X:
        while h_idx < Y:
            now += heal[h_idx]
            h_idx += 1
            ans.append(h_idx)
        break

if len(ans) == X + Y:
    for i in ans:
        print(i)
else:
    print(0)
