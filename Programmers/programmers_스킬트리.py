def solution(skill, skill_trees):
    answer = 0
    # 각 스킬트리에 있는 목록
    for check_skill in skill_trees:
        # skill의 index
        idx = 0
        # 배울 수 있는 스킬인지 여부 판단
        check = True
        # 문자열 하나하나 skill과 비교
        for alpha in check_skill:
            # 알파벳이 skill안에 존재 할 때를 검사한다.
            # 존재하지 않으면 넘어가도 상관없음
            if alpha in skill:
                # idx로 skill의 앞부분부터 검사하고 배웠다면 idx 증가
                if alpha == skill[idx]:
                    idx += 1
                # 순서대로 배우지 않았다면 끝
                else:
                    check = False
                    break
        # 순서대로 배웠다면 가능한 스킬트리로 갯수 증가
        if check:
            answer += 1

    return answer