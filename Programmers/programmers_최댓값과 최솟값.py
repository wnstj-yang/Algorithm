def solution(s):
    answer = ''
    # 공백기준으로 숫자들을 구분하여 각각 문자열을 정수형으로 바꾸고 리스트형태로 만든다
    num_list = list(map(int, s.split(' ')))
    answer += str(min(num_list)) + ' ' # 최솟값 저장
    answer += str(max(num_list)) # 최댓값 저장
    return answer