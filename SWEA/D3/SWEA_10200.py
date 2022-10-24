# SW Expert Academy - 10200번. 구독자 전쟁

T = int(input())

for tc in range(1, T + 1):
    N, A, B = map(int, input().split())
    min_val, max_val = 987654321, 0
    min_val = (A + B) - N # 두 수를 합하고 전체 인원 N을 뺐을 때 0보다 크다면 최소 그 인원 수가 둘 다 구독한다는 의미
    if min_val < 0: # 0보다 작다면 최소 인원은 0
        min_val = 0
    max_val = min(A, B)
    print('#{} {} {}'.format(tc, max_val, min_val))
