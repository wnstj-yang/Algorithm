# Baekjoon Online Judge - 20154번. 이 구역의 승자는 누구야?!

alpha_line = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

S = list(input())
# 대문자 알파벳을 값으로 바꿔준다
for i in range(len(S)):
    S[i] = alpha_line[ord(S[i])-65]

# 하나가 남을 때 까지 계속해서 돌려준다
while len(S) != 1:
    result = []
    # 짝지어지도록 만든다
    for i in range(0, len(S), 2):
        # 리스트 인덱싱 시 범위가 벗어나도 끝을 의미해준다
        val = sum(S[i:i+2])
        # 10을 벗어나면 10으로 나머지 값 구하기
        if val >= 10:
            val %= 10
        result.append(val)
    S = result

if S[0] % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")
