# SW Expert Academy - 1983번. 조교의 성적 매기기

T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    k_val = 0 # 내림차순 정렬 전 K 번째 학생의 총점을 알아야 한다. 
    numbers = []
    for i in range(1, N + 1):
        mid, final, assign = map(int, input().split())
        numbers.append(mid * 0.35 + final * 0.45 + assign * 0.2)
        if i == K:
            k_val = numbers[i - 1]
    numbers.sort(reverse=True)
    length = N // 10
    # 총점이 동일한 경우는 없기 때문에 해당 총점으로 인덱스를 찾은 이후에 내림차순 정렬된 것 순으로 등급을 출력
    print('#{} {}'.format(tc, grade[numbers.index(k_val) // length]))
