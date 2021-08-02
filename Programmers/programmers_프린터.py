def solution(priorities, location):
    answer = 0
    # 우선순위와 일종의 인덱스를 튜플로 넣는다.
    target = []
    for i in range(len(priorities)):
        target.append((priorities[i], i))
    # 우선순위만 있는 것은 정렬을 해줘서 내림차순으로
    priorities.sort(reverse=True)
    while True:
        prior, value = target.pop(0)
        # 맨 앞이 우선순위가 제일 높음
        # 현재의 우선순위가 제일 높은 우선순위가 같거나 크다면
        # 바로 꺼낸다
        if prior >= priorities[0]:
            answer += 1
            # 그러면 가장 큰 우선순위가 나가져버린다.
            priorities.pop(0)
            if value == location:
                break
        # 그렇지 않으면(중요도 높은 문서가 한 개라도 존재) 맨 뒤에 추가
        else:
            target.append((prior, value))

    return answer