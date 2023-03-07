# 정렬 - 유형별. 안테나 360p

N = int(input())
homes = list(map(int, input().split()))
homes.sort()
# 가운데에서 뺴는 값들이 최소가 되더라도 왼쪽에 있는 것이 더 작을 수있기 때문에 1을 빼준다.
print(homes[(N - 1) // 2])
