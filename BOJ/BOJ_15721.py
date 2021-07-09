# Baekjoon Online Judge - 15721번. 번데기

A = int(input())
T = int(input())
target = int(input())
ans = []
n = 2
idx = 0
cnt = 0
end = False
while True:
    check = True
    cnt = 0
    # check를 통해 0, 1, 0, 1(뻔, 데기 뻔, 데기)를 넣어준다
    for i in range(4):
        if check:
            ans.append(0)
            check = False
        else:
            ans.append(1)
            check = True

    # n-1회차 만큼 뻔을 넣어줌
    for i in range(n):
        ans.append(0)

    # n-1회차 만큼 데기를 넣어줌
    for i in range(n):
        ans.append(1)

    # cnt를 통해 몇번 째인지 개수를 세준다
    for i in range(len(ans)):
        if ans[i] == target:
            cnt += 1
            # 정답이라면 몇번째 사람인지 나누기 연산으로 표현
            if cnt == T:
                end = True
                print(i % A)
                break

    if end:
        break
    # 회차 증가
    n += 1
