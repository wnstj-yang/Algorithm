# Baekjoon Online Judge - 1120번. 문자열


A, B = map(str, input().split())
result = 987654321
# 문제에서처럼 따로 알파벳을 추가하지 않고 A의 길이를 B의 길이의 처음부터 A길이만큼 비교해서 최소값을 찾는다
for i in range(len(B) - len(A) + 1):
    cnt = 0
    for j in range(len(A)):
        if B[i + j] != A[j]:
            cnt += 1
    result = min(result, cnt)
print(result)
