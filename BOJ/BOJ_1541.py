# Baekjoon Online Judge - 1541번. 잃어버린 괄호

equation = input()
equation = equation.split('-') # -를 기준으로 나눈다.
result = []
for num in equation:
    _sum = 0
    # +가 있다면 괄호로 감싼다는 의미임(최소값을 위해서)
    if '+' in num:
        num = num.split('+') # +를 기준으로 나누고
        # 각각 더해준다
        for n in num:
            _sum += int(n)
        result.append(_sum)
    # 단순히 숫자라면 리스트에 추가
    else:
        result.append(int(num))
# 첫 숫자를 넣어주고
answer = result[0]
# 이후의 숫자들을 빼준다(미리 '-'를 기준으로 나누었고, '+'가 있으면 괄호로 묶어줘서 안의 값들을 다 더해준 것으로 전처리함)
for num in result[1:]:
    answer -= num
print(answer)
