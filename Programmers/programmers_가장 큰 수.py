def solution(numbers):
    # for문으로도 가능하지만 map함수 이용하여 str으로 변환
    numbers = list(map(str, numbers))
    # 각 숫자는 1000이하 이므로 문자열로된 숫자를 3을 곱해서 3자리 수 이상으로 만든다
    # [3, 30, 34, 5, 9]의 경우에서 정렬 시  [9,5,34,30,3] 이 만들어지기 때문에
    # [999, 555, 343434, 333, 303030]처럼 만들어서 내림차순 정렬을 해준다
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))