# Baekjoon Online Judge - 3649번. 로봇 프로젝트
import sys
input = sys.stdin.readline

# 여러 개의 테스트케이스로 이루어져 있다는 표현이 있으므로 try except문으로 처리
while True:
    try:
        x = int(input()) * int(1e7) # 센치미터에서 나노미터로 환산
        n = int(input())
        lego_length = []

        for _ in range(n):
            l = int(input())
            lego_length.append(l)
        start, end = 0, len(lego_length) - 1
        check = False
        lego_length.sort()
        # 겹치는 문제가 생기면 안되기 때문에 부등호에 같다는 표시를 안해야 한다.
        while start < end:
            length = lego_length[start] + lego_length[end]
            # 두 개의 길이를 합한 것을 찾았다면 끝
            if length == x:
                check = True
                break
            else:
                # 두 개의 길이 합이 구멍보다 크다면 끝에서부터 인덱스를 1 빼준다
                if length >= x:
                    end -= 1
                # 작다면 길이를 늘려야 하므로 앞의 인덱스를 1 더해준다.
                else:
                    start += 1
        if check:
            print('yes {} {}'.format(lego_length[start], lego_length[end]))
        else:
            print('danger')
    except:
        break

