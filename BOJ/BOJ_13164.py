# Baekjoon Online Judge - 13164번. 행복 유치원
# 조를 나눠서 진행하면 시간초과 발생

N, K = map(int, input().split())
students = list(map(int, input().split()))
ans = 0
diff = []
for i in range(1, N):
    diff.append(students[i] - students[i-1])
# 차이를 내림차순으로 정렬
diff.sort()
ans = sum(diff[:N-K])
print(ans)
# 5 2
# 1 3 5 6 10
# 위와 같은 경우 (1, 3, 5, 6), (10)
# 각 조의 양끝을 빼는 것은 안의 요소들 빼기를 합한 것과 같다
# Ex) 1-3 + 5-3 + 6-5 == 6 - 1
# diff : 1 2 2 4
# 그래서 각각 빼준 것을 diff에 넣고 정렬을 해준다음 최소 값을
# N-K까지의 합을 구한다 diff 기준 !
