def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)


def solution(n, k):
    answer = []
    k -= 1 # 0번째부터 시작이므로 1을 빼준다.
    numbers = [i for i in range(1, n + 1)]
    for i in range(n, 0, -1):
        # k를 몫과 나머지를 구하고, 몫은 numbers의 인덱스, 나머지는 k의 업데이트를 한다.
        # 나누는것은 factorial(i - 1)인데, n이 3일 때 0번째 수가 바뀔 때 (n-1)!번이 든다.
        # 앞 자리 수가 결정되면 하나씩 수를 줄여나가면서 인덱스와 수를 구하게 된다.
        # 1) k = 4, q = 2, r = 0, (3-1)! = 2, answer = [3], numbers = [1, 2]
        # 2) k = 0, q = 0, r = 0, (2-1)! = 1, answer = [3, 1], numbers = [2]
        # 3) k = 0, q = 0, r = 0, (1-1)! = 1, answer = [3, 1, 2], numbers = []
        q, r = divmod(k, factorial(i - 1))
        answer.append(numbers.pop(q))
        k = r
    return answer
