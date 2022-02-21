# Baekjoon Online Judge - 4256번. 트리


def postorder(left, right, root):

    for i in range(left, right):
        if preorder[root] == inorder[i]:
            # 왼쪽 서브트리
            postorder(left, i, root + 1)
            # 오른쪽 서브트리
            postorder(i + 1, right, root + i + 1 - left)
            print(preorder[root], end=' ')


T = int(input())
for _ in range(T):
    N = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder(0, N, 0)
    print()
