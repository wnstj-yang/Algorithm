# Baekjoon Online Judge - 1357번. 뒤집힌 덧셈

X, Y = map(str, input().split())
X = int(X[::-1]) # [start:stop:step]
Y = int(Y[::-1])
result = str(X + Y)[::-1]
print(int(result))
