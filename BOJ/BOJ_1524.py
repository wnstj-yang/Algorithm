# Baekjoon Online Judge - 1524번. 세준세비

T = int(input())

for _ in range(T):
    space = input()
    N, M = map(int, input().split())
    sj = list(map(int, input().split()))
    sb = list(map(int, input().split()))
    max_sj = max(sj)
    max_sb = max(sb)
    # 가장 약한 병사들이 죽으면서 최후에 1명이 남는 것을 고려한다는 것이 마지막엔 가장 강한 사람들이 남는다
    # 그래서 세비가 가장 강하면 이기고, 가장 강한 사람이 양측에 있거나 세준에 있다면 세준이 이긴다
    if max_sj < max_sb:
        print('B')
    elif max_sj >= max_sb:
        print('S')
