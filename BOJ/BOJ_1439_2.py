# Baekjoon Online Judge - 1439번. 뒤집기

number = input()
zero_cnt, one_cnt = 0, 0
for i in range(1, len(number)):
    if number[i - 1] != number[i]:
        if number[i - 1] == '0':
            one_cnt += 1
        else:
            zero_cnt += 1

if number[-1] == '0':
    one_cnt += 1
else:
    zero_cnt += 1
print(min(zero_cnt, one_cnt))
