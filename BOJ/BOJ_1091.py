# Baekjoon Online Judge - 1091번. 카드 섞기

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
original = [0, 1, 2] * (N // 3)
num_list = set()
result = 0
# 0 ~ N - 1번 카드를 또 만드는 것 대신 존재한다는 가정 하 P를 활용한다.
# 즉, 최종적으로 P수열 처럼 만들어지도록 카드를 섞는 것이기 때문이다.
while original != P:
    temp = [0] * N
    # i번 위치가 S[i]번째 위치로 이동
    for i in range(N):
        temp[S[i]] = P[i]
    P = temp
    # 돌고돌아 만들지 못하는 경우를 대비해서 목록에 있다면 결국 카드를 섞어도 원하는 값을 구하지 못하는 것
    if tuple(P) not in num_list:
        num_list.add(tuple(P))
    else:
        result = -1
        break
    result += 1
print(result)
