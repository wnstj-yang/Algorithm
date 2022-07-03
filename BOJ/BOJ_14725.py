# Baekjoon Online Judge 14725번. 개미굴

ant_houses = []
N = int(input())
for _ in range(N):
    info = list(input().split())
    ant_houses.append(info[1:])
# 사전 순서대로이기 때문에 정렬 진행
ant_houses.sort()
floor = '--'
for i in range(N):
    # 첫 번째의 경우 출력을 진행해서 이후의 것들과 비교
    if i == 0:
        for j in range(len(ant_houses[i])):
            print(floor * j + ant_houses[i][j])
    else:
        cnt = 0 # 중복되는 것들을 제외한 이후의 인덱스(몇 번째인지)
        for j in range(len(ant_houses[i])):
            # 이전 정보의 길이가 현재 정보의 길이보다 작아야함(인덱스 상)
            # 그리고 이전 정보의 현재 위치와 현재 정보의 위치와 다른 경우 끝
            if j < len(ant_houses[i - 1]) and ant_houses[i - 1][j] != ant_houses[i][j]:
                break
            else:
                # 중복되지 않는 것들을 바탕으로 현재 인덱스 처리
                cnt = j + 1
        # 위의 과정을 거쳐서 현재 인덱스부터 남아있는 현재 정보의 내용을 출력
        for j in range(cnt, len(ant_houses[i])):
            print(floor * j + ant_houses[i][j])
