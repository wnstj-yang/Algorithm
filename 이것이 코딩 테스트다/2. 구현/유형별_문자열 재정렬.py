# 유형별 문제 2. 문자열 재정렬 - 322p

string = input()
result = []
number = 0
for value in string:
    # 알파벳과 숫자를 분리해서 각각 더해준다
    if value.isalpha():
        result.append(value)
    else:
        number += int(value)
result.sort() # 오름차순 정렬
# 정렬이된 이후의 리스트는 문자열로 만들고 뒤에 합해진 숫자를 더해준다
if number == 0:
    print(''.join(result))
else:
    print(''.join(result) + str(number))


# 입력 - 1
# K1KA5CB7
# 출력 - 1
# ABCKK13

# 입력 - 2
# AJKDLSI412K4JSJ9D
# 출력 - 2
# ADDIJJJKKLSS20
