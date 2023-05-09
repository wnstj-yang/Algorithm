def solution(food):
    answer = ''
    num = 1 # 인덱스이자 수를 나타낸다.
    for f in food[1:]: # 0번은 물의 번호이므로 1번부터 진행
        answer += str(num) * (int(f) // 2) # num의 수를 f(음식의 개수)를 2로 나눈다.
        # 2로 나누는 것은 물(0)을 기준으로 왼쪽에는 순서대로, 오른쪽에는 뒤집은 결과를 붙여주기 위함이다.
        num += 1 # 인덱스 증가
    # 필요한 음식들의 배치 + 물 + 필요한 음식들의 배치 뒤집은 결과
    answer = answer + '0' + answer[::-1]
    return answer
