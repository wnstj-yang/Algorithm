# Bakejoon Online Judge - 17255번. N으로 만들기
# 투포인터, 왼쪽, 오른쪽, result에는 N으로 만들어짐, full에다가
# "숫자를 적는 과정에서 나온 수가 순서대로 모두 같다면 같은 방법이다"를 생각
# 1 ----(앞에 1이 붙음)----> 11 ----(앞에 9가 붙음)----> 911 ----(뒤에 1이 붙음)----> 9111
# 1 ----(뒤에 1이 붙음)----> 11 ----(앞에 9가 붙음)----> 911 ----(뒤에 1이 붙음)----> 9111
# 위의 예시처럼 2개가 아닌 1개여야 함. 그래서 full에 1119119111처럼 하나의 붙여진 string을 만들어서 set에 넣어준다

def check(l, r, result, full):
    if l == 0 and r == len(N) - 1:
        get_ans.add(full)
        return
    # 왼쪽에다가 계속 더해주다가
    if l - 1 >= 0:
        check(l-1, r, N[l-1] + result, full+N[l-1]+result)
    # 오른쪽에도 붙여준다
    if r + 1 < len(N):
        check(l, r + 1, result+N[r+1], full+result+N[r+1])


N = list(input())
get_ans = set()
for i in range(len(N)):
    check(i, i, N[i], N[i])
print(len(get_ans))
