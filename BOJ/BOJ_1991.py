# Baekjoon Online Judge - 1991번. 트리 순회 => Again

# 전위순회
def preorder(n):
    if n != 0:
        print(node[n], end='')
        preorder(node.index(child[n][0]))
        preorder(node.index(child[n][1]))


# 중위순회
def inorder(n):
    if n != 0:
        inorder(node.index(child[n][0]))
        print(node[n], end='')
        inorder(node.index(child[n][1]))


# 후위순회
def postorder(n):
    if n != 0:
        postorder(node.index(child[n][0]))
        postorder(node.index(child[n][1]))
        print(node[n], end='')


N = int(input())
# node와 child를 초기화 해준다
node = [0] * (N+1)
child = [[0] * 2 for _ in range(N+1)]

for i in range(1, N+1):
    info = input().split()
    # 입력된 값( 부모인 것을 node의 값에 넣는다 )
    node[i] = info[0]

    if child[i][0] == 0:
        # 왼쪽 자식이 존재한다면 넣어줌
        if info[1] != '.':
            child[i][0] = info[1]

    if child[i][1] == 0:
        # 오른쪽 자식이 존재하면 넣어줌
        if info[2] != '.':
            child[i][1] = info[2]

# node에 각 알파벳이 들어있고, 이를 index를 통해 각 전위, 중위, 후위 순회를 진행한다.
preorder(node.index('A'))
print()
inorder(node.index('A'))
print()
postorder(node.index('A'))
print()

