# Baekjoon Online Judge - 1931번. 회의실 배정

# 그리디 문제

N = int(input())
conferences = []
for _ in range(N):
    start, end = map(int, input().split())
    conferences.append((start, end))
# 끝나는 시간을 기준으로 정렬하고 시간 시간으로 정렬
# 시작 시간도 정렬하는 이유는 끝나는 시간이 같고 시작 시간이 다른 경우들이 존재하기에 시작 시간도 정렬
conferences.sort(key=lambda x: (x[1], x[0]))

end_time = 0
answer = 0
for start, end in conferences:
    # 회의실 정렬 상태에서 회의 끝난 시간보다 시작 시간이 크거나 같은 경우 업데이트
    if start >= end_time:
        end_time = end
        answer += 1
print(answer)

