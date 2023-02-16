# 이것이 코딩 테스트다 - 4장 정렬 실전문제 4. 두 배열의 원소 교체 182p

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)
for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))

# 5 3
# 1 2 5 4 3
# 5 5 6 6 5