# Baekjoon Online Judge - 19583번. 싸이버개강총회

# 그냥 input으로 할 시 try - except로 입력이 끝날때 까지 진행해야한다.
# 아니면 아래와 같이 sys 모듈을 가져와서
import sys
# sys.stdin.readline => 끝 부분까지 가져온다
input = sys.stdin.readline

S, E, Q = map(str, input().split())
S = int(''.join(S.split(':')))
E = int(''.join(E.split(':')))
Q = int(''.join(Q.split(':')))
students = {}
ans = 0
while True:
    data = input()
    # 나눌 수 없는 길이까지 온다면 끝
    if len(data) < 5:
        break
    time, name = data.split()
    time = int(''.join(time.split(':')))
    # 첫 시작까지 사람 체크
    if time <= S:
        students[name] = 1
    # 끝난시간 과 스트리밍 시간 전까지 체크
    elif E <= time <= Q:
        # 해당 학생이 시작에 있다면 회원 체크
        if name in students and students[name] == 1:
            ans += 1
            students[name] = 0
print(ans)
