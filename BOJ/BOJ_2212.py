# Baekjoon Online Judge - 2212번. 센서

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
# Ex) 1 6 9 3 6 7 => 1 3 6 6 7 9의 센서 정렬
sensors.sort()
distances = []
# 집중국들이 센서들보다 크면 X
if K > N:
    print(0)
else:
    # 1. 인접한 센서들의 거리를 구합니다.
    for i in range(len(sensors) - 1):
        distances.append(sensors[i + 1] - sensors[i])
    # 2. 구한 거리들이 있을 때 가장 큰 값을 기준으로 집중국을 설치
    # Ex) 구한 거리는 2 3 0 1 2이여서 K가 2일 때 3을 기준으로 나누면 [1, 3], [6, 9]로 묶인다.
    # 각 좌표들의 안의 센서들은 집중국에 연결.
    # 편의상 2 3 0 1 2 => 3 2 2 1 0으로 내림차순 정렬을 통해
    distances.sort(reverse=True)
    # 3. 정렬된 거리들에서 가장 큰 값들을 빼서 나머지 거리들의 합을 구한다.
    # 빼는 것 대신 0으로 초기화. 3 2 2 1 0 => 0 2 2 1 0
    for i in range(K - 1):
        distances[i] = 0
    print(sum(distances))
