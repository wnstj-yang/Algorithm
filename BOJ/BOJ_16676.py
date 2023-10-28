# Baekjoon Online Judge - 16676번. 근우의 다이어리 꾸미기

N = input()
s = '1' * len(N)

if int(N) < 10:
    print(1)
else:
    # 이게 N을 최댓값으로 하기 때문에 N이 123이라도 111을 만족해야 하므로 최소3개여야한다.
    if int(N) >= int(s):
        print(len(N))
    else:
        print(len(N) - 1) # 기준인 1, 11, 111 보다 작으면 그 이전 개수로 처리
