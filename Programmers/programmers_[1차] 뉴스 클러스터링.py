def make_only_alphabets(string):
    temp = []
    for i in range(len(string) - 1):
        # 연속되는 두 문자열이 영문자일 때 리스트에 담는다
        if string[i].isalpha() and string[i + 1].isalpha():
            temp.append(string[i:i + 2])
    return temp


def solution(str1, str2):
    answer = 0
    # 1. 모두 소문자로 바꾼다(대문자도 가능)
    str1 = str1.lower()
    str2 = str2.lower()

    # 2-1. 다중집합 만들기
    str1_list = make_only_alphabets(str1)
    str2_list = make_only_alphabets(str2)

    # 2-2. 각각 문자열 리스트들의 교집합과 합집합을 구한다. (이 때 중복이 제거됨)
    union_list = set(str1_list) | set(str2_list)
    intersection_list = set(str1_list) & set(str2_list)
    union, intersection = 0, 0
    # 3. 중복 제거된 교집합 합집합으로 다시 역으로 개수를 더해준다

    # 합집합 구할 때 두 문자열 리스트 중에 개수가 최대인 것을 더해준다(둘 중 하나라도 있어도 최대 개수)
    for string in union_list:
        union += max(str1_list.count(string), str2_list.count(string))

    # 교집합 구할 때 두 문자열 리스트 중에 개수가 최소인 것을 더해준다 (둘 다 있는 것 중에서 최소 개수)
    for string in union_list:
        intersection += min(str1_list.count(string), str2_list.count(string))

    # 0으로 나누지 못하면 65536 return
    if union == 0:
        answer = 65536
    else:
        answer = int((intersection / union) * 65536)
    return answer
