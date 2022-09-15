# Baekjoon Online Judge - 1581번. 락스타 락동호

ff, fs, sf, ss = map(int, input().split())
# 빠른 노래가 없는 경우
if ff == 0 and fs == 0:
    # 빠르게 끝나는 것이 없다면 ss의 수가 최대
    if sf == 0:
        print(ss)
    # 빠르게 끝나는 것이 있다면 ss의 수 최대로 한 다음 마지막에 1개 추가(1개 이유는 그 뒤에 노래 추가를 할 수 없기 때문)
    else:
        print(ss + 1)
# 빠르게 시작하고 느리게 끝난 것이 없다면 1번 조건에 따라 빠르게 끝나는 ff개수가 맞다. 그래야 최대가 됨
elif fs == 0:
    print(ff)
# 빠르게 끝나는 노래들이 존재할 때
else:
    # fs와 sf를 기준으로 잡는 것은 ff와 ss는 스스로 개수를 늘릴 수 있다.
    # fs가 sf보다 작거나 같을 때 fs를 기준으로 해당 수 만큼 늘리고 나머지를 더한다.
    if fs <= sf:
        print(ff + 2 * fs + ss)
    # fs가 더 크다면 맨 앞의 1개를 추가하고 나머지는 그보다 적은 sf를 기준으로 2를 곱해서 늘리고 나머지를 더한다.
    else:
        print(ff + 2 * sf + ss + 1)

