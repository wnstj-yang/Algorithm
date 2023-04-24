# Baekjoon Online Judge - 11256번. 사탕

T = int(input()) # 출력 개수

for _ in range(T):
    answer = 0
    j, N = map(int, input().split()) # 사탕의 개수 : j, 상자의 개수 : N
    boxes = [] # 상자의 크기 담을 리스트
    for _ in range(N):
        R, C = map(int, input().split()) # 각 상자의 가로 세로 길이
        boxes.append(R * C) # 가로 세로의 곱을 리스트에 넣음(용량)
    boxes.sort(reverse=True) # 내림차순 정렬으로 큰 것 부터 사탕의 개수를 넣는다
    for box in boxes:
        j -= box # 사탕의 개수 - 박스의 용량
        answer += 1 # 박스의 개수를 늘린다
        if j <= 0: # 0보다 작거나 같으면 사탕의 개수가 없으므로 끝
            break
    print(answer)
