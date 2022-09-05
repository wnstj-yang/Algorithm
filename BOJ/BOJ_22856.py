# Baekjoon Online Judge 22856번. 트리 순회
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def inorder(x):
    global cnt
    if x != -1:
        inorder(tree[x][0])
        inorder_list.append(x)
        inorder(tree[x][1])


def like_inorder(x):
    global cnt

    if tree[x][0] != -1:
        cnt += 1
        like_inorder(tree[x][0])

    if x == end_node:
        print(cnt)
        exit(0)
        return

    cnt += 1  # 지나가는 노드
    if tree[x][1] != -1:
        like_inorder(tree[x][1])
        cnt += 1


N = int(input())
tree = [[0] * 2 for _ in range(N + 1)]
inorder_list = []
cnt = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    tree[a][0] = b
    tree[a][1] = c
inorder(1)
end_node = inorder_list[-1]
like_inorder(1)


