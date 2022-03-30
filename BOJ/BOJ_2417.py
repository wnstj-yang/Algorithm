# Baekjoon Online Judge - 2417번. 정수 제곱근

n = int(input())
start = 0
end = n
answer = n
while start <= end:
    q = (start + end) // 2
    # 가장 작은 음이 아닌 정수 q를 출력해야 하므로 구하고 끝이 아니라 최소 값을 구해나가야한다.
    if q ** 2 >= n:
        answer = min(answer, q)
    # q 제곱 값이 n보다 작은 경우 시작점 증가
    if q ** 2 < n:
        start = q + 1
    # n보다 크면 끝 점 감소
    else:
        end = q - 1
print(answer)
