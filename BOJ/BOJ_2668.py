# Baekjoon Online Judge - 2668번. 숫자고르기

# 단순한 DFS로 할 경우 시간 초과 발생
# 사이클을 찾아야한다.


def dfs(indexes, values, number):
    indexes.add(number)
    values.add(arr[number])
    if arr[number] in indexes: # 해당 부분이 있어야 무한루프를 벗어난다. 사이클 확인 유무 판단 - 값 중 하나가 인덱스에 있는지 확인(사이클)
        if indexes == values:
            result.update(indexes)
        return
    return dfs(indexes, values, arr[number])


N = int(input())
arr = [0]
for _ in range(N):
    arr.append(int(input()))
result = set()
# 사이클을 찾는다. 즉, 1,3 끼리 사이클, 5 혼자 사이클 => 인덱스와 값이 같음을 확인
# 그래서 1부터 시작해서 사이클인 수들을 넣는다
for i in range(1, N + 1):
    if i not in result:
        dfs(set(), set(), i)
result = list(result)
print(len(result))
result.sort()
for i in result:
    print(i)
