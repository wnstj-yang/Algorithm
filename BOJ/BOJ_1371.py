# Baekjoon Online Judge - 1371번. 가장 많은 글자
import sys

# EOF(End Of File)까지 입력을 받아준다
words = sys.stdin.read()
alpha = [0] * 26
for word in words:
    if word.isalpha():
        alpha[ord(word) - 97] += 1

max_num = max(alpha)
for i in range(26):
    if max_num == alpha[i]:
        print(chr(i + 97), end='')
