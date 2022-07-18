# Baekjoon Online Judge - 1268번. 임시 반장 정하기

N = int(input())
students = [[0] * (N + 1) for _ in range(N + 1)]
grade = [list(map(int, input().split())) for _ in range(N)]
result = [0] * (N + 1)
# i 학년 ( 사실 상 i + 1학년으로 인식해야 덜 헷갈림 )
for i in range(5):
    # j번째 학생
    for j in range(1, N + 1):
        # j + 1번째 부터 N + 1까지의 학생과의 비교
        for k in range(j + 1, N + 1):
            # i학년 j번째 학생과 i학년 k번째 학생이 같은 반이라면 표시
            # 인덱스 상으로 1을 빼줘서 계산
            if grade[j - 1][i] == grade[k - 1][i]:
                # 중복 방지
                students[j][k] = 1
                students[k][j] = 1

for i in range(1, N + 1):
    result[i] = students[i].count(1)

answer = result.index(max(result))
if answer:
    print(answer)
else:
    print(1) # 인덱스가 0번일 때가 예외라서 1로 출력


