# Baekjoon Online Judge - 1764번. 듣보잡
# 시간이 오래 걸린다
N, M = map(int, input().split())
name_list = dict()
for i in range(N+M):
    name = input()
    # 하나의 딕셔너리안에 같은 이름이 있다면 추가 count, 없다면 1
    if name not in name_list:
        name_list[name] = 1
    else:
        name_list[name] += 1

ans = []
for name in name_list:
    # 듣보잡이 되야하니 이름이 하나만 나오면 답이 아니다
    if name_list[name] != 1:
        ans.append(name)
# 정렬
ans.sort()
print(len(ans))
# print('\n'.join(ans))
for name in ans:
    print(name)
