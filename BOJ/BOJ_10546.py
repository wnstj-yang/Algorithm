# Baekjoon Online Judge - 10546. 배부른 마라토너
# pypy3에서만 통과

N = int(input())
marathoners = {}
for i in range(N):
    name = input()
    # 마라토너 동명이인도 구분위해 명수 카운트
    if name not in marathoners:
        marathoners[name] = 1
    else:
        marathoners[name] += 1

# 통과한 마라토너는 수를 줄인다.
for i in range(N-1):
    pass_name = input()
    marathoners[pass_name] -= 1

# 통과하지 못한 마라토너를 찾아 출력
for participant in marathoners:
    if marathoners[participant] != 0:
        print(participant)
        break


