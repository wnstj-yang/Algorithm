# Baekjoon Online Judge - 1213번. 팰린드롬 만들기
# 참고... 팰린드롬은 주어진 문자열 중에 홀수 개가 2개 이상이면 안된다.


name = list(input())
alphabets = [0] * 26
answer = ''
odd_alpha = ''
odd = 0
for a in name:
    alphabets[ord(a) - 65] += 1

for i in range(26):
    if alphabets[i] % 2 == 1:
        odd_alpha = chr(i + 65)
        odd += 1
    answer += chr(i + 65) * (alphabets[i] // 2)

reversed_name = list(answer)
reversed_name.reverse()

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(''.join(answer) + odd_alpha + ''.join(reversed_name))
