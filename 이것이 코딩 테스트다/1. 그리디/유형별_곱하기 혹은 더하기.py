# 유형별 문제 2. 곱하기 혹은 더하기 - 312p

S = input()
# 0 혹은 1이면 더해준다. 2부터 9까지는 곱해줌. 0을 곱하면 값이 작아지고, 1이면 그대로이니 더해주는 것임
result = int(S[0])
for i in range(1, len(S)):
    num = int(S[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)

# 입력 - 1
# 02984
# 출력 - 1
# 576

# 입력 - 2
# 567
# 출력 - 2
# 210
