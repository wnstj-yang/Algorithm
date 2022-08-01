# Baekjoon Online Judge - 1526번. 가장 큰 금민수


N = int(input())
result = 0
# 4와 7이 각 자리수에 있다면 끝내고, 아니면 N에서 1씩 줄여가면서 최대값을 찾아나선다
while True:
    found = True
    number = str(N)
    for i in number:
        if i != '4' and i != '7':
            found = False
            N -= 1
    if found:
        print(N)
        break
