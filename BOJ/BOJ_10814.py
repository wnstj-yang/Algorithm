# Baekjoon Online Judge - 10814번. 나이순 정렬

N = int(input())
info = []
for i in range(N):
    x, y = input().split()
    # index를 따로 넣어 나이가 같을 때 가입한 순으로 조정 가능
    info.append((int(x), y))
# 정렬 시 나이 순으로 정렬이 되고 가입한 순서대로 만들어지기 때문에
# 나이 순으로만 정렬
info.sort(key=lambda x: x[0])
for item in info:
    print(item[0], item[1])
