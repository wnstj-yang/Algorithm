# Baekjoon Online Judge - 20164번. 홀수 홀릭 호석

def check(num, result):
    global min_val, max_val

    if len(num) == 1:
        min_val = min(min_val, result)
        max_val = max(max_val, result)

    elif len(num) == 2:
        odd = 0
        cal_result = int(num[0]) + int(num[1])
        for i in str(cal_result):
            if int(i) % 2 == 1:
                odd += 1

        check(str(cal_result), result + odd)
    else:
        for l in range(len(num) - 2):
            for r in range(l + 1, len(num) - 1):
                a = int(num[:l + 1])
                b = int(num[l + 1:r + 1])
                c = int(num[r + 1:])
                cal_result = a + b + c
                odd = 0
                for i in str(cal_result):
                    if int(i) % 2 == 1:
                        odd += 1
                check(str(cal_result), result + odd)


N = input()
min_val = 987654321
max_val = 0
first_odd = 0
for i in N:
    if int(i) % 2 == 1:
        first_odd += 1
check(N, first_odd)
print(min_val, max_val)
