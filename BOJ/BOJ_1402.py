# Baekjoon Online Judge - 1402번. 아무래도이문제는A번난이도인것같다

T = int(input())

# 사실상 A를 B로 무조건 바꿀 수 있다. 1와 -1 등을 활용하면서 덧셈 시 가능하기 때문
for _ in range(T):
    A, B = map(int, input().split())
    print('yes')
