def solution(brown, yellow):
    answer = []
    # 약수 구하기
    target = []
    result = brown + yellow
    # 약수를 구한다
    for i in range(1, 2000001):
        if i > result:
            break
        if result % i == 0:
            target.append(i)
    # 약수의 값중 끝에서(큰값)부터 가로로생각하고 세로를 구한다
    for i in range(len(target)-1, -1, -1):
        # target[i]가 가로, height가 세로
        height = result // target[i]
        # yellow의 수가 맞는지 확인한다. brown을 감싸는 것인지 확인하기 때문
        if (target[i] - 2) * (height - 2) == yellow:
            answer.append(target[i])
            answer.append(height)
            break
    return answer

# 수학적으로도 접근 가능
# x: 가로 / y: 세로
# brown = 2x + 2(y-2) = 2(x+y-2)
# yellow = (x-2) * (y-2)