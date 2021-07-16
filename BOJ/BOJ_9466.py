# Baekjoon Online Judge - 9466번. 텀 프로젝트
# 반례 => 팀이라고해서 1->2->3->1 만 팀이 아니라 1->2->3->2 처럼도 팀이 될 수 있음 ...

from collections import deque

T = int(input())

for tc in range(T):
    n = int(input())
    students = [0] * (n + 1)
    temp = list(map(int, input().split()))
    temp_idx = 1
    for i in temp:
        students[temp_idx] = i
        temp_idx += 1
    # 방문 표시
    visited = [0] * (n + 1)
    # 팀으로 만들어진 학생 수를 cnt한다.
    cnt = 0
    for i in range(1, n+1):
        # 방문하는 학생과 선택한 학생이 같다면 혼자 팀을 이룬다.
        if i == students[i] and visited[i] == 0:
            cnt += 1
            visited[i] = 1
            continue
        else:
            # 혼자 팀을 이루지 않는다면
            if visited[i] == 0:
                # stack으로 방문할 수 있는 학생들을 넣는다.
                stack = deque()
                # checked_list로 팀 가능성이 있는 학생들을 넣는다.
                checked_list = [i]
                stack.append(i)
                idx = 0
                while stack:
                    x = stack.pop()
                    visited[x] = 1
                    # 현재 방문하는 학생이 선택한 학생을 방문하지 않았다면 팀이 될 가능성이 있음
                    if visited[students[x]] == 0:
                        stack.append(students[x])
                        checked_list.append(students[x])
                    else:
                        # 팀 가능성이 있는 학생들 중에 선택한 학생이 존재하면 팀이 이루어진 것임
                        if students[x] in checked_list:
                            # 팀으로 이루어졌을 때의 학생 index를 구해서 몇명인지 cnt해서 더한다.
                            idx = checked_list.index(students[x])
                            cnt += len(checked_list[idx:])
                            break
    # 전체 학생 수 - 팀으로 이루어진 학생 수
    print(n-cnt)
