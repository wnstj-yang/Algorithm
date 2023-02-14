# Baekjoon Online Judge - 11478번. 서로 다른 부분 문자열의 개수

S = input()
result = set()
for i in range(1, len(S) + 1):
    for j in range(len(S)):
        result.add(S[j:j+i])
print(len(result))
