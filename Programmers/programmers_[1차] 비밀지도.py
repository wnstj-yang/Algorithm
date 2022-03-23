def dec_to_bin(number, n):
    n_str = ''
    while number != 0:
        n_str = str(number % 2) + n_str
        number = number // 2
    # n의 길이만큼 이진수 변환이 안되어있다면 앞에 0을 (n 길이 - 구한 이진수 길이)만큼 추가해준다
    if len(n_str) != n:
        n_str = '0' * (n - len(n_str)) + n_str
    return n_str


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1_num = dec_to_bin(arr1[i], n)
        arr2_num = dec_to_bin(arr2[i], n)
        result = ''

        for i in range(n):
            # 숫자가 같을 때 1인지 0인지 판단해서 벽 혹은 공백 추가
            if arr1_num[i] == arr2_num[i]:
                if arr1_num[i] == '1':
                    result += '#'
                else:
                    result += ' '
            # 둘이 다르다면 벽으로 판단
            else:
                result += '#'
        answer.append(result)

    return answer
