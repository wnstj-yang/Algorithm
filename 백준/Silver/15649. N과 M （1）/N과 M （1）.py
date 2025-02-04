from itertools import permutations

N, M = map(int, input().split())
arr = list(range(1, N+1))
permute = list(permutations(arr, M))
for i in permute:
    print(*i)