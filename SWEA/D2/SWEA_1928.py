# SW Expert Academy - 1928번. Base64 Decoder

T = int(input())
info = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
]
# 인코딩 시 8비트씩 나누어서 나열해놓고 6비트씩 쪼개서 위의 인코딩 방식에 따라 문자를 인코딩함
# 24비트면 8비트가 3개의 문자, 그러면 6비트씩 잘랐을 때 4개의 문자로 인코딩이 진행됨 
for tc in range(1, T + 1):
    words = list(input())
    mid_process = ''
    for word in words:
        num = info.index(word)
        bin_num = bin(num)[2:]
        # 이진수로 표현 시 6비트씩 나눠야 하므로 부족한 부분은 앞에 0을 필요한 개수만큼 추가함
        if len(bin_num) < 6:
            bin_num = '0' * (6 - len(bin_num)) + bin_num
        mid_process += bin_num
        
    result = ''
    # 디코딩 시 8비트씩 잘라서 아스키코드에 맞게 변환
    for i in range(0, len(mid_process), 8):
        num = chr(int(mid_process[i:i+8], 2))
        result += num
    print('#{} {}'.format(tc, result))
