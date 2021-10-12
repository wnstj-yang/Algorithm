# Baekjoon Online Judge - 5567번. 결혼식


def dfs(s, cnt):
    # 시작노드를 제외해서 depth 2까지 진행하여서 set 중복 방지
    if s != 1:
        friend.add(s)
    # depth가 2까지 구해야함. 친구의 친구까지를 구한다
    if cnt == 2:
        return
    for i in friends[s]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, cnt+1)
            # 한 줄기에 중복되는 노드가 있을 수 있는 것 방지
            visited[i] = 0


n = int(input())
m = int(input())
friends = [[] for _ in range(n+1)]
visited = [0] * (n+1)
friend = set()

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
visited[1] = 1
dfs(1, 0)
print(len(friend))
