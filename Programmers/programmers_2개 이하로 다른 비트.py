def solution(numbers):
    answer = []
    # 주어진 수 + 1부터 큰 수를 찾아나설 때 범위가 커지므로 단순 접근 X
    # 짝수와 홀수로 나누어 규칙성이 존재한다.
    for number in numbers:
        # 홀수일 때 마지막에서부터 0을 찾는다.
        # 그 다음 0 -> 1, 마지막 다음의 숫자가 1이므로 이를 0으로 바꾼다
        # 즉, 01 -> 10
        if number % 2:
            num = bin(number)
            target = list('0' + num[2:])
            for i in range(len(target) - 1, -1, -1):
                if target[i] == '0':
                    target[i] = '1'
                    target[i+1] = '0'
                    answer.append(int('0b' + ''.join(target), 2))
                    break
        # 짝수면 맨뒤에 1만 추가되므로 + 1해주면 된다
        else:
            answer.append(number+1)
    return answer