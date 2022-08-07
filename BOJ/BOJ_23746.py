# Baekjoon Online Judge - 23746번. 문자열 압축 해제

N = int(input())
string_list = {}

for _ in range(N):
    a, b = map(str, input().split())
    string_list[b] = a
string = input()
result = ''
S, E = map(int, input().split())
for alpha in string:
    result += string_list[alpha]
print(result[S-1:E])
