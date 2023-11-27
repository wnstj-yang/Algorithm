# Baekjoon Online Judge - 1269번. 대칭 차집합

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
# set으로 된 차집합은 각각 집합 자료형에서 빼기를 진행해주면 된다.
print(len(A - B) + len(B - A))
