N = int(input())
balloons = list(map(int, input().split()))
result = []
indexes = [i + 1 for i in range(N)]

index = 0
val = balloons.pop(index)
result.append(indexes.pop(index))
# 규칙이 아래와 같다.
while balloons:
    # 하나씩 줄어드니 오른쪽 방향일 때 인덱싱을 1을 줄인다.
    # pop할 시 리스트가 앞으로 당겨져서 한 칸 덜 이동 한다.
    if val > 0:
        index = (index + val - 1) % len(balloons)
    # 왼쪽으로 가는 경우에는 그대로 해도 된다.
    # pop이 되지만, 리스트 순서가 당겨지진 않는다.
    else:
        index = (index + val) % len(balloons)
    val = balloons.pop(index)
    result.append(indexes.pop(index))
print(*result)

