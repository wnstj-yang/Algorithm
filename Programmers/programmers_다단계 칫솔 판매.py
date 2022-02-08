def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    index = {}
    for i in range(len(enroll)):
        index[enroll[i]] = i
    for i in range(len(seller)):
        # index[name] : 현재 노드(인덱스)
        # referral[index[name]] : 부모 노드(문자열)
        name = seller[i]
        price = amount[i] * 100  # 초기값
        answer[index[name]] += price
        while referral[index[name]] != '-':  # 루트 노드까지 찾는 것
            answer[index[name]] -= (price // 10)  # 10% 현재 노드에서 뺀다
            name = referral[index[name]]  # 부모 노드로 바꿔준다
            answer[index[name]] += (price // 10)  # 10% 부모 노드에 더해준다
            price //= 10  # 10%된 금액으로 초기화
            if price == 0:
                break

        # 루트 노드를 부모로 갖고 있을 때
        answer[index[name]] -= price // 10

    return answer