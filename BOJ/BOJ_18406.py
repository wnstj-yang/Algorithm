# Baekjoon Online Judge - 18406번. 럭키 스트레이트


N = input()
left, right = 0, 0
# 왼쪽과 오른쪽 자릿수들을 비교해서 합이 같거나 다른지 판단
for i in range(len(N)):
    if i < len(N) // 2:
        left += int(N[i])
    else:
        right += int(N[i])
if left == right:
    print("LUCKY")
else:
    print("READY")
