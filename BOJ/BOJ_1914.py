# Baekjoon Online Judge - 1914번. 하노이 탑

def hanoi(circle, depart, via, arrive):
    global cnt
    if circle == 1:  # 원반 하나일 때 시작 기둥에서 도착 기둥
        print(depart, arrive)
        return
    hanoi(circle - 1, depart, arrive, via)  # 1번 기둥에 있는 원반들을 2번으로(3번 기둥 보조)
    print(depart, arrive) # 가장 큰 원반 이동(1번 기둥에 남아있는)
    hanoi(circle - 1, via, depart, arrive)  # 2번 기둥에 있는 원반들을 3번으로(1번 기둥 보조)


N = int(input())
print((2 ** N) - 1) # 2^(N-1) - 1의 식이 옮긴 횟수
if N <= 20:
    hanoi(N, 1, 2, 3)
