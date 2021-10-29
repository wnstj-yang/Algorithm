# Bakejoon Online Judge - 11000번. 강의실 배정
import heapq

N = int(input())
num_list = []
ans_list = []
for _ in range(N):
    x, y = map(int, input().split())
    num_list.append([x, y])
num_list.sort()
# heapq를 사용해서 시간, 메모리 초과를 방지한다.
# (1, 3)에서 뒤에 시간(3)을 넣어준다.
# (2, 4)에서 heapq에 들어간 3보다 앞의 시간(2)이 작으면 새로운 회의실 배정(뒤의 시간 넣는다 4)
# (3, 5)에서 heapq는 최소가 맨 앞에 오므로 3과 같다. 그러면 하나의 회의실로 가능하니 5로 초기화해준다.(3 -> 5)
heapq.heappush(ans_list, num_list[0][1])
for i in range(1, len(num_list)):
    if num_list[i][0] < ans_list[0]:
        heapq.heappush(ans_list, num_list[i][1])
    else:
        heapq.heappop(ans_list)
        heapq.heappush(ans_list, num_list[i][1])
print(len(ans_list))
