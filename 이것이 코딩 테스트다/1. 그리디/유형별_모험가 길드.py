# 유형별 문제 1. 모험가 길드 - 311p

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
result = 0
X = 0
# 오름차순으로 정렬 후 작은 것부터 그룹으로 묶어나가서 최대 그룹 개수를 구한다.
for num in numbers:
    X += 1 # 사람 수 카운트
    # 공포도 num이 X명 이상으로 구성이 되었다면 그룹으로 묶고 아니면 사람 수 계속 카운트
    # 1 2 2 2 3일 때 그룹 1 => 1, 그룹 2 => (2, 2), 그룹 3은 2에서 사람 수 1, 3에서 사람 수가 2인데 3까지 가질 못하므로
    # 총 그룹은 2개임
    if X >= num:
        result += 1
        X = 0
print(result)

# 입력 - 1
# 5
# 2 3 1 2 2
# 출력 - 1
# 2