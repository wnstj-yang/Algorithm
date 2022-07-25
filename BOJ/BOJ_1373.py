# Baekjoon Online Judge - 1373번. 2진수 8진수

# 2진수 -> 10진수 -> 8진수의 형식으로 가면 시간 초과 발생
# 2진수 -> 8진수로 바꿀때 2진수의 3자리가 8이기 때문에 뒤에서부터 3자리씩 끊어준다
# 안나누어지면 0으로 채워넣음 
# Ex) 1101 => '00'1 / 101로 나눈다
binary = input()
oct_num = ''
binary = binary[::-1]
for i in range(0, len(binary), 3):
    bin_num = binary[i:i+3]
    if len(bin_num) < 3:
        bin_num += '0' * (3 - len(bin_num))
    num = 1
    temp = 0
    for b in bin_num:
        temp += (int(b) * num)
        num *= 2
    oct_num += str(temp)
print(oct_num[::-1])
