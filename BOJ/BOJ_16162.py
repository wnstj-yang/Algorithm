# Baekjoon Online Judge - 16162번. 가희와 3단 고음

N, A, D = map(int, input().split())
numbers = list(map(int, input().split()))
X = 0
cnt = 0
# 첫 항을 발견하고 나서 부터 등차를 이루는 숫자가 있는지만 확인하면 된다.
for num in numbers:
    # 공차로 잘 이루어지는지 확인
    if num == A + (cnt * D):
        cnt += 1
        X += 1
print(X)
