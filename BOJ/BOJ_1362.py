# Baekjoon Online Judge - 1362번. 펫

idx = 1
while True:
    o, w = map(str, input().split())
    if o == '0' and w == '0':
        break
    o = int(o)
    w = int(w)
    while True:
        order, num = map(str, input().split())
        if order == '#' and num == '0':
            if w <= 0:
                print('{} RIP'.format(idx))
            elif o / 2 < w < o * 2:
                print('{} :-)'.format(idx))
            else:
                print('{} :-('.format(idx))
            idx += 1
            break
        if w > 0:
            if order == 'F':
                w += int(num)
            else:
                w -= int(num)

