# Baekjoon Online Judge - 1181번. 단어 정렬
# 시간이 좀 많이 걸리는 단점 존재

N = int(input())
words = []
for i in range(N):
    word = input()
    length = len(word)
    if (word, length) not in words:
        words.append((word, length))

# 길이가 짧은 순으로 정렬하고, 문자 순으로 다시 정렬
ans = sorted(words, key = lambda x : (x[1], x[0]))
for i in range(len(ans)):
    print(ans[i][0])
