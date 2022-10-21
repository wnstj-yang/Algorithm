# SW Expert Academy - 11285번. 다트 게임
import math


T = int(input())
answer = []
for tc in range(1, T + 1):
    N = int(input())
    result = 0
    for _ in range(N):
        # 원의 방정식을 활용해서 점수를 구한다.
        x, y = map(int, input().split())
        # 거듭제곱인 **은 시간복잡도가 O(N)임...
        loc = math.ceil(math.sqrt(x * x + y * y) / 20)
        if loc <= 0:
            result += 10
        elif loc <= 11:
            result += 11 - loc
    answer.append(f'#{tc} {result}') # 이 것 또한 해주어야 시간초과 발생 X
for ans in answer:
    print(ans)

