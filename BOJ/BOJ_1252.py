# Baekjoon Online Judge - 1252번. 이진수 덧셈

A, B = input().split()
A, B = list(map(int, A)), list(map(int, B))
# B가 더 큰 것으로 만들고, A와 비교했을 때 부족한 부분은 0으로 채워넣는다
if len(A) > len(B):
    B, A = A, B
for i in range(len(B) - len(A)):
    A = [0] + A

# 연산을 위해 A, B 각 이진수는 모두 반대로 만든다.
A.reverse()
B.reverse()
answer = []
carry = 0 # 올림 수가 있는지 판단

for i in range(len(B)):
    # 각 인덱스마다 올림 수가 있는 지 각각 더해준다
    result = A[i] + B[i] + carry
    # 2 이상이면 올림 수가 있어야 하므로 만들어주고, 2를 빼서 현재 위치의 값을 구한다
    if result >= 2:
        carry = 1
        answer.append(str(result - 2))
    else:
        carry = 0
        answer.append(str(result))
# 남은 올림 수가 존재하면 추가한다.
if carry:
    answer.append(str(1))

# 처음부터 뒤바꿔서 연산을 했기 때문에 이를 다시 되돌린다.
answer.reverse()

# 이진수에서 앞부분에서부터 1을 찾아서 다음의 수들을 출력
# 그 앞부분의 0들은 의미가 없기 때문에 출력하지 않는다.
idx = 0
for i in range(len(answer)):
    if answer[i] == '1':
        idx = i
        break
if idx == 0 and answer[idx] == '0':
    print(0)
else:
    print(''.join(answer[idx:]))

