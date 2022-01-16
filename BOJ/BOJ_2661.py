# Baekjoon Online Judge - 2661번. 좋은수열

# 애초에 재귀돌 때 최소값부터 진행하므로 찾으면 그것이 정답이다
# idx가 N 즉, N만큼의 수부터 재귀를 하는 것이 아니라
# idx가 N이 되면 최소임을 나타나기 위해 그 이전의 값들의 경우 나쁜수열들을 미리 없앤다.
def check(idx):
    for i in range(1, idx // 2 + 1): # 비교할 길이
        for j in range(idx - (i * 2) + 1): # 길이에 맞춘 범위 ( 총 길이에서 2로 나눈 것을 참고 )
            if numbers[j:i + j] == numbers[i + j:i + i + j]:
                return False
    if idx == N:
        print(''.join(numbers))
        return True
    for i in range(1, 4):
        numbers.append(str(i))
        result = check(idx+1)
        if result:
            return 1
        numbers.pop()


N = int(input())
numbers = []

check(0)
