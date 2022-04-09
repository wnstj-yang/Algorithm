# Baekjoon Online Judge - 2108번. 통계학
import sys
input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()
# 1. 산술평균 - round를 통해 소수점 에서 반올림
print(round(sum(numbers) / len(numbers)))
# 2. 중앙값 - 이전에 정렬을 했으므로 중간 값을 구함 
print(numbers[len(numbers) // 2]) 
numbers_cnt = {}
# 각 주어진 수의 개수를 구한다. (Ex. -1: 3이면 -1이 3개)
for i in range(len(numbers)):
    if numbers[i] not in numbers_cnt:
        numbers_cnt[numbers[i]] = 1
    else:
        numbers_cnt[numbers[i]] += 1
# 최빈값을 구하기 위해 최빈값대로 내림차순 정렬 후 여러 개일 때 두 번째로 작은 값을 출력해야하므로 값은 오름차순으로 정렬
numbers_cnt = sorted(numbers_cnt.items(), key=lambda x: (-x[1], x[0]))

# 3. 최빈값 - 개수가 1개면 값 출력, 2개 이상인 경우 최빈 값이 같은 것이 2개 이상인지 확인해서 조건에 맞게 출력
if len(numbers_cnt) == 1:
    print(numbers_cnt[0][0])
else:
    if numbers_cnt[0][1] == numbers_cnt[1][1]:
        print(numbers_cnt[1][0])
    else:
        print(numbers_cnt[0][0])

# 4. 범위 - 최댓값 - 최소값
print(numbers[-1] - numbers[0])
