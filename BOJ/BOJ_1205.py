# Baekjoon Online Judge - 1205번. 등수 구하기

N, new_score, P = map(int, input().split())
answer = -1
# 0인 것과 아닌 것으로 나눈다.
if N == 0:
    if P > 0:
        answer = 1
else:
    # 점수들을 입력받는다
    scores = list(map(int, input().split()))
    ranks = [1] # 첫 번째는 등수가 1이며 입력받은 점수들의 랭킹을 기록
    cnt = 1 # 다음 등수를 갱신하는 변수
    now = scores[0] # 현재 등수를 가리키는 값
    same = 0 # 같은 등수의 값이 몇개 있는지 확인
    for score in scores[1:]:
        #
        if score < now:
            cnt = cnt + same + 1 # 다음 등수를 적는다(현재 등수 + 여태까지 같은 값을 가진 개수 + 다음 등수를 말하는 1)
            now = score # 현재 등수 값 갱신
            ranks.append(cnt) #
            same = 0 # 초기화
        # 값이 같다면 같은 개수 추가 및 등수는 그대로
        elif score == now:
            ranks.append(cnt)
            same += 1

    changed = False
    for i in range(N):
        score = scores[i]
        # 새로운 값이 현재 값보다 크고 P가 N보다 크거나 같으면 넣을 수 있다.
        if new_score > score and P >= N:
            # 이전 것과 같으면 등수는 이전 등수로
            if new_score == scores[i - 1]:
                answer = ranks[i - 1]
            # 그 외에 새로운 값이 더 크다면 현재 등수로 대체
            else:
                answer = ranks[i]
            changed = True
            break

    # 바꾸지 못했을 때 
    if not changed:
        # 추가할 수 있는 경우
        if P > N:
            # 값이 마지막과 같으면 등수는 동일
            if new_score == scores[-1]:
                answer = ranks[-1]
            # 추가하는 경우 그 이전까지 진행되었던 등수를 바탕으로 갱신
            else:
                answer = cnt + same + 1
print(answer)
