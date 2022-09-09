# Baekjoon Online Judge - 1107번. 리모컨

N = int(input())
M = int(input())
buttons = [str(i) for i in range(10)]
# 리모컨에 고장난 번호들 처리
if M > 0:
    broken_bts = list(map(int, input().split()))
    for b in broken_bts:
        buttons.remove(str(b))


min_cnt = abs(N - 100) # 값을 찾을 때 가장 최대값부터 시작
# 100만으로 잡는 이유는 최대가 50만인데 0 -> 50만, 100만 -> 50만 처럼 최대값을 기준으로 +, -로 갈 수 있는 최대 수가 100만이다.
for channel in range(1000001):
    check = True
    # 리모컨에 고장난 번호를 건드린다면 다음으로 넘어간다
    for i in str(channel):
        if i not in buttons:
            check = False
            break
    # 고장난 번호가 없는 상태라면 현재 채널에서 목표 N을 뺀 후 절댓값 처리와 해당 채널 자릿수 길이를 더해준다(번호 클릭 횟수)
    if check:
        min_cnt = min(min_cnt, abs(channel - N) + len(str(channel)))
print(min_cnt)
