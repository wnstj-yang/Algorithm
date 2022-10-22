# Baekjoon Online Judge - 14425번. 문자열 집합

N, M = map(int, input().split())
# 리스트로 할 때의 시간 복잡도 차이가 크다. set()으로 지정
string_list = set()
for _ in range(N):
    string_list.add(input())
result = 0
for _ in range(M):
    string = input()
    # in을 돌릴 때 튜플일 때 시간복잡도가 줄음
    if string in string_list:
        result += 1
print(result)