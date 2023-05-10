


def solution(number, limit, power):
    answer = 0
    divisors = [] # 각 기사의 약수의 개수를 넣어준다
    for num in range(1, number + 1): # 번호 순서대로 진행
        cnt = 0 # 약수의 개수
        # 약수를 구할 때 해당 수의 범위를 끝까지 하게 되면 시간복잡도가 O(N^2)이 발생하여 시간초과가 된다
        # 그래서 제곱근을 활용하여 약 O(N)정도로 줄인다. O(N^0.5*N)?
        for i in range(1, int(num ** 0.5) + 1):
            # 현재 숫자를 i로 나누었을 때 0이면 약수를 의미한다.
            if num % i == 0:
                # 제곱근의 경우 약수가 딱 하나이기 때문에 1을 증가
                if i ** 2 == num:
                    cnt += 1
                # 그 이외에 (a, b), (b, a)처럼 2개의 경우가 나오기에 2를 더해준다
                else:
                    cnt += 2
        divisors.append(cnt) # 해당 기사의 약수의 개수를 넣음
    # 각 약수의 개수를 반복문에 적용
    for num in divisors:
        # 제한수치보다 크다면 그에 해당하는 공격력을 더해주고 아니면 약수의 개수(기사의 공격력)를 더해준다
        if num > limit:
            answer += power
        else:
            answer += num
    return answer
