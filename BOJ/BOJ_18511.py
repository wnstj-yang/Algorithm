# Baekjoon Online Judge - 18511번. 큰 수 구성하기

def check(n, d):
    global result
    if n == d:
        num = int(''.join(ans))
        # N보다 작거나 같고 기존보다 커야함
        if result < num <= N:
            result = num
        return
    for i in elements:
        ans.append(i)
        check(n+1, d)
        ans.pop()


N, K = map(int, input().split())
elements = list(input().split())
ans = []
result = 0
# 중요한 부분 !
# K원소의 수 까지가 아니라 K 원소의 수 들로 N자리 수 만큼 진행해서
# 최대 값을 구한다
for k in range(1, len(str(N))+1):
    check(0, k)
print(result)
