def solution(arr):
    answer = 0
    arr.sort(reverse=True) # 내림차순 정렬
    for i in range(len(arr) - 1):
        n, m = arr[i], arr[i+1] # 두 수를 갖고 최대공약수
        while m > 0:
            n, m = m, n % m
        # 만들어진 최대공약수 n 을 통해 최소공배수를 구하고
        # 구해진 것을 다음 인덱스에 넣어 이후에도 진행을 한다.
        arr[i+1] = (arr[i] * arr[i+1]) // n
    answer = arr[-1] # 가장 마지막 값이 최소공배수
    return answer