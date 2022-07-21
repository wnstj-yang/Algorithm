# Baekjoon Online Judge - 1333번. 부재중 전화


N, L, D = map(int, input().split())
time = [0] * ((N * (L + 5)) - 5)
# 노래가 끝나고 5초 동안은 전화를 받을 수 있는 상태로 만든다.
for i in range(L, len(time), L + 5):
    for j in range(i, i + 5):
        time[j] = 1
idx = D
# 전화벨 시간 간격마다 전화를 받을 수 있는 상태인지 판단
while idx < len(time):
    if time[idx]:
        break
    idx += D
print(idx)
