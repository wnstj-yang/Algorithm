# Baekjoon Online Judge - 16719번. ZOAC
# 추가했을 때의 문자열을 비교하는 것이다


def check(l, r):
    # l과 r이 같다면 탐색할 것이 없음(끝)
    if l == r:
        return
    # 사전 순 가장 앞에 오는것 
    min_str = min(str_list[l:r])
    # 중복되는 문자가 있을 수 있어서 l, r활용 리스트의 범위 사용하고 위치를 더한다.
    min_idx = str_list[l:r].index(min_str) + l

    visited[min_idx] = True
    for i in range(len(str_list)):
        if visited[i]:
            print(str_list[i], end='')
    print()
    # 사전 순의 값 기준으로 오른쪽, 왼쪽 범위 탐색 
    check(min_idx + 1, r)
    check(l, min_idx)


str_list = list(input())
visited = [False] * len(str_list)
check(0, len(str_list))
