# Baekjoon Online Judge - 11656번. 접미사 배열

S = input()
ans = []
for i in range(len(S)):
    ans.append(S[i:])
ans.sort()
for i in range(len(S)):
    print(ans[i])
