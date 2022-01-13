# Baekjoon Online Judge - 1174번. 줄어드는 수
from itertools import combinations

n = int(input())
numbers = []
# 9876543210이 마지막 수 이므로 10자리 수까지
for i in range(1, 11):
    # 규칙성이 조합을 나타낸다. 각각의 조합을 구하고 내림차순으로 만들어준다
    for item in combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], i):
        item = list(item) # 튜플로 반환되니까 리스트로
        item.sort(reverse=True)
        numbers.append(int(''.join(map(str, item))))
# 한 번 더 정렬해주지 않으면 10 20 30 이렇게 나오기 때문에 10 20 21 30 31 처럼 만들어준다
numbers.sort()
# 9876543210까지 총 1024개가 존재하고 인덱스에 따라 출력
if n >= 1024:
    print(-1)
else:
    print(numbers[n - 1])
