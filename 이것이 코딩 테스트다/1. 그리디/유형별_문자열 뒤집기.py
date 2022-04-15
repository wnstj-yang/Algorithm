# 유형별 문제 3. 문자열 뒤집기 - 313p

S = input()
cnt_0, cnt_1 = 0, 0
# 모두 0 혹은 1로 바꿀 때 최소 횟수 비교해서 답으로 정한다.
for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        if S[i] == '1':
            cnt_1 += 1
        else:
            cnt_0 += 1
# 마지막 것까지 비교해서 횟수에 넣는다
if S[-1] == '1':
    cnt_1 += 1
else:
    cnt_0 += 1
print(min(cnt_1, cnt_0))

# 입력 - 1
# 0001100
# 출력 - 1
# 1
