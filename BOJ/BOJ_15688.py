# Baekjoon Online Judge - 15688번. 수 정렬하기 5
# 그냥 input() 사용시 시간 초과 / pypy3로 통과
# 음의 정수도 있기에 메모리 100만에서 200만으로 증가
import sys
numbers = [0] * 2000001

N = int(input())
for _ in range(N):
    num = int(sys.stdin.readline())
    # 음의 정수 있기에 100만을 더한다
    numbers[num + 1000000] += 1

for i in range(2000001):
    if numbers[i] > 0:
        for j in range(numbers[i]):
            # 출력할 때는 더했던 값을 다시 빼준다
            print(i - 1000000)
