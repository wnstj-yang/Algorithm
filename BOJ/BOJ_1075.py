# Baekjoon Online Judge - 1075번. 나누기

N = input()
F = int(input())

start = int(N[:-2] + '00')
while True:
    if start % F == 0:
        start = str(start)
        print(start[-2:])
        break
    else:
        start += 1
