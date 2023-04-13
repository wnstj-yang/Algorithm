def solution(numbers):
    result = list(map(str, numbers))
    # 문자열로 바꾸고 3을 곱한 상태에서 정렬하는 이유
    # 9, 991이 있다고했을 때 9가 더 앞에와야 하나 숫자로 하면 뒤에 오게 된다.
    # 그래서 문자열로 999, 991991991을 비교해서 큰 값을 찾아서 앞에 정렬시킨다.
    # 원소가 1000이하이기때문에 3을 곱해준다
    result.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(result)))