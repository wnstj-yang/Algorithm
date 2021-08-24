# Baekjoon Online Judge - 20154번. 이 구역의 승자는 누구야?!

alpha_line = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

S = list(input())
ans = 0
for i in range(len(S)):
    # 대문자 알파벳을 바꿈과 동시에 값들을 다 구해주고 나머지 10으로 처리해준다
    S[i] = alpha_line[ord(S[i])-65]
    ans += S[i]
    if ans >= 10:
        ans %= 10

if ans % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")
