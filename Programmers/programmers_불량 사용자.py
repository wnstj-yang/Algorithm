# 조합
def check_ans(idx, k, visited, ans, ans_candi, banned):
    if idx == k:
        # 정렬을 해주어야 set에 들어갈 때 중복없이 가능
        align = sorted(ans)
        # set을 사용 시 안의 순서가 바뀌는 것임(랜덤)
        if tuple(align) not in ans_candi:
            ans_candi.add(tuple(align))
        return
    # 조합 부분
    for item in banned[idx]:
        if not visited[item]:
            visited[item] = True
            ans[idx] = item
            check_ans(idx + 1, k, visited, ans, ans_candi, banned)
            visited[item] = False


def solution(user_id, banned_id):
    answer = 0
    banned = [[] for _ in range(len(banned_id))]
    # 불량 사용자들 각각을 전체 사용자들과 가능성을 비교한다
    # banned_id에 있는 거를 index로 정한다
    for b_idx in range(len(banned_id)):
        # 각 불량 사용자 아이디를 구한다
        b_id = banned_id[b_idx]
        for u_idx in range(len(user_id)):
            check = True
            user = user_id[u_idx]
            # 길이가 같다면 불량 사용자인지 판단
            if len(user) == len(b_id):
                for i in range(len(b_id)):
                    if b_id[i] == '*':
                        continue
                    if b_id[i] != user[i]:
                        check = False
                        break
                if check:
                    banned[b_idx].append(u_idx)
    # 정답 후보
    ans_candi = set()
    # 방문
    visited = [False] * len(user_id)
    # ans에 각 사용자 인덱스를 넣어서 순서 확인
    ans = [0] * len(banned_id)
    check_ans(0, len(banned_id), visited, ans, ans_candi, banned)
    answer = len(ans_candi)

    return answer