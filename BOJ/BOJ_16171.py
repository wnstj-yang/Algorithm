# Baekjoon Online Judge - 16171번. 나는 친구가 적다 (Small)

S = input()
K = input()
only_str = ''
# 숫자이면 넘어가고 알파벳이면 문자열이니 only_str에 추가한다
for i in S:
    if 48 <= ord(i) <= 57:
        continue
    else:
        only_str += i

# 키워드 문자열, 숫자제외 문자열로만 구성된 문자열의 각각 길이를 구한다
length_str = len(only_str)
length_K = len(K)

# 키워드 문자열보다 길이가 크거나 같을 때
if length_str >= length_K:
    # 각 문자열 길이가 같고 키워드 문자열인지 check
    if length_str == length_K:
        if only_str == K:
            print(1)
        else:
            print(0)
    else:
        check = False
        # 키워드 문자열을 길이만큼 비교하면서 똑같은 것이 있는지 체크한다.
        for i in range(length_str-length_K+1):
            if only_str[i:i+length_K] == K:
                check = True
                break
        if check:
            print(1)
        else:
            print(0)

# 키워드 문자열 길이보다 작으면 끝
else:
    print(0)
