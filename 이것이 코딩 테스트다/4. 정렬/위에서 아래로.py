# 이것이 코딩 테스트다 - 4장 정렬 실전문제 2. 위에서 아래로 178p

N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))
numbers.sort(reverse=True)
print(*numbers)


# 3
# 15
# 27
# 12
