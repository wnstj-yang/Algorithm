# Baekjoon Online Judge - 1032번. 명령 프롬프트

N = int(input())
result = ''
cmds = []
for _ in range(N):
    cmds.append(input())

length = len(cmds[0])
for j in range(length):
    check = False
    check_string = cmds[0][j]
    for i in range(1, N):
        if cmds[i][j] != check_string:
            check = True
            break
    if check:
        result += '?'
    else:
        result += check_string
print(result)

