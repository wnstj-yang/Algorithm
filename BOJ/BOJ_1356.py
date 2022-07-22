# Baekjoon Online Judge - 1356번. 유진수

N = input()
# 인덱스를 통해 각 문자열마다 자르면서 왼쪽과 오른쪽의 자릿수 합이 똑같은 것이 있다면 유진수로 판단
check = False
for i in range(1, len(N)):
    left = N[:i]
    right = N[i:]
    l_sum, r_sum = 1, 1
    
    for l in left:
        l_sum *= int(l)
    for r in right:
        r_sum *= int(r)
    if l_sum == r_sum:
        check = True
        break
if check:
    print('YES')
else:
    print('NO')
