# Baekjoon Online Judge - 2138번. 전구와 스위치


def change(num):
    if num:
        return 0
    else:
        return 1


def check(k, switch):
    # 0번 스위치를 눌렀을 때와 안눌렀을 때 구분해서 진행
    # 비교할 이전 전구가 없기 때문에 두 경우로 나눈다
    cnt = k
    if k == 1:
        switch[0] = change(switch[0])
        switch[1] = change(switch[1])
    # 현재 전구 상태가 이전 전구 상태에 영향을 줄 수 있기 때문에 만들고자 하는 상태에 맞게 순차 진행
    # 되돌아오면서 다시 상태를 바꾼다고 해서 target과 같아지지 않아 회숫만 늘어나게 된다
    for i in range(1, len(switch)):
        if switch[i - 1] != target[i - 1]:
            cnt += 1
            switch[i - 1] = change(switch[i - 1])
            switch[i] = change(switch[i])
            if i < len(switch) - 1:
                switch[i + 1] = change(switch[i + 1])
    if switch == target:
        return cnt
    else:
        return 987654321


N = int(input())
now = list(map(int, input()))
target = list(map(int, input()))
# Python은 리스트나 딕셔너리 같은 데이터형(튜플 제외)이 매개변수로 전달될 때 레퍼런스에 의한 호출
result = min(check(0, now[:]), check(1, now[:]))
if result == 987654321:
    print(-1)
else:
    print(result)
