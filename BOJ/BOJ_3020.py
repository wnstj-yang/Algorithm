# Baekjoon Online Judge - 3020번. 개똥벌레
# sys모듈 사용 안할 시 pypy3로만 통과
# import sys
# input = sys.stdin.readline

N, H = map(int, input().split())

top = [0] * (H + 1)
bottom = [0] * (H + 1)
min_val = 987654321 #
cnt = 0
for i in range(N):
    num = int(input())
    # 홀수 : 종유석인 경우
    if i % 2:
        top[num] += 1
    # 짝수 : 석순인 경우
    else:
        bottom[num] += 1

# 크기가 큰 것부터 해서 누적 합으로 몇 개인지 체크
for i in range(H - 1, 0, -1):
    top[i] += top[i + 1]
    bottom[i] += bottom[i + 1]

# 몇 번째 구간(높이)에서 개똥벌레가 날아가서 파괴하는 장애물 수 구하기
for i in range(1, H + 1):
    # 종유석(top)경우 높이에서 현재 구간을 뺀 후 1을 더한 값과 석순(bottom)의 개수와 더한 것이 파괴한 장애물 수이다.
    result = bottom[i] + top[H - i + 1]
    if result < min_val:
        min_val = result
        cnt = 1
    elif result == min_val:
        cnt += 1
print(min_val, cnt)
