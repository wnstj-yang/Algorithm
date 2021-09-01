# Baekjoon Online Judge - 5568번. 카드 놓기


def check(cnt):
    #
    if cnt == k:
        ans.add(''.join(result))
        return
    for i in range(n):
        # 순열이기 때문에 중복 방지를 visited 이용
        if visited[i] == 0:
            visited[i] = 1
            # result에 k개수만큼의 수를 넣는다.
            result.append(numbers[i])
            check(cnt+1)
            # 순열 개수 중 하나 끝나면 뒤에거를 pop
            result.pop()
            visited[i] = 0


n = int(input())
k = int(input())
numbers = []
for _ in range(n):
    numbers.append(input())

result = []
visited = [0] * n
ans = set()
check(0)
print(len(ans))
