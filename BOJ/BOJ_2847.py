# Baekjoon Online Judge - 2847번. 게임을 만든 동준이

N = int(input())
numbers = []
answer = 0
for _ in range(N):
    numbers.append(int(input()))

# 끝에서 부터 줄여 나간다
for i in range(N - 1, 0, -1):
    # 끝에서부터 앞에 값이 뒤의 값보다 크거나 같다면 오름차순을 위해 줄여줘야 한다.
    if numbers[i - 1] >= numbers[i]:
        answer += (numbers[i - 1] - numbers[i] + 1) # 앞(큰 값) - 뒤(현재, 작은 값) + 1(아래 1빼준 값을 더한다)
        numbers[i - 1] = numbers[i] - 1 # 최소로 볼 수 있는 뒤의 값(현재)에서 1을 빼준다
print(answer)
