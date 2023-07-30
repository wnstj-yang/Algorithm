def solution(topping):
    answer = 0
    # 리스트 슬라이싱을 하고 set으로 만들다보니 공간을 만들면서 시간도 늘어나기에 시간복잡도가 높은듯 하다
    # for i in range(1, len(topping) - 1):
    #     left, right = set(topping[:i]), set(topping[i:])
    #     if len(left) == len(right):
    #         answer += 1

    # 딕셔너리 활용
    left = {}
    # 우선 모든 토핑들 왼쪽이라는 딕셔너리로 숫자 : 갯수로 넣는다
    for i in topping:
        if i in left:
            left[i] += 1
        else:
            left[i] = 1

    # 오른쪽으로 지나가면서 오른쪽의 딕셔너리에 토핑은 추가하고 왼쪽은 삭제해준다
    right = {}
    for i in range(len(topping)):
        # 왼쪽의 개수와 오른쪽의 개수가 같다면 공평하게 나눈 것이다
        if len(left) == len(right):
            answer += 1
        # 왼쪽, 오른쪽으로 나누는 것이기 때문에 right에 현재 토핑값의 유무에 따라 개수 설정
        if topping[i] not in right:
            right[topping[i]] = 1
        else:
            right[topping[i]] += 1

        # 기존에 left에있었던 것을 지우고 개수가 0이면 없애준다
        left[topping[i]] -= 1
        if left[topping[i]] == 0:
            del left[topping[i]]

    return answer