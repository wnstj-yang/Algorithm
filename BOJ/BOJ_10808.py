# Baekjoon Online Judge - 10808번. 알파벳 개수

alpha_cnt = [0] * 26

word = input()

for alpha in word:
    # 알파벳이 소문자로 이루어져있어서 97을 뺴준다. 아스키코드
    alpha_cnt[ord(alpha)-97] += 1
print(*alpha_cnt)
