# Baekjoon Online Judge - 1568번. 새

N = int(input())
result = 0
time = 1
while N != 0:
    # 나무에 어떤 숫자(시간)보다 적게 있다면 1로 초기화해서 다시 진행한다. 오름차순으로
    if time > N:
        time = 1
    else:
        N -= time
        time += 1
        result += 1
print(result)
