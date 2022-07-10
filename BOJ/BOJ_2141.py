# Baekjoon Online Judge - 2141번. 우체국

N = int(input())
numbers = []
people = 0 # 전체 인원 수
for _ in range(N):
    X, A = map(int, input().split())
    numbers.append((X, A))
    people += A
# 집 번호의 수에 따라 정렬
numbers.sort(key=lambda x: x[0])
cnt = 0
for i in range(N):
    cnt += numbers[i][1]
    # // 2로 하면 내림으로 기존 인원 나누기 2에서의 계산이 제대로 되지 않는다.
    # 그래서 기존 / 2를 통해 우체국 설치 위치를 구함
    # 총 인원의 중간 값을 찾아야 거리의 합이 최소가 되는 위치를 구할 수 있다.
    if cnt >= people / 2:
        print(numbers[i][0])
        break