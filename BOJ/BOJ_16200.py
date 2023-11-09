# Baekjoon Online Judge - 16200번. 해커톤

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort() # 오름차순 정렬
result = 0 # 결과값
limit = 0 # 정렬 이후 i번째의 첫번째 값을 기준으로 순회하면서 제한을 두기 위한 값. 즉, 팀의 팀원들 중 최소 명수가 필요한 값
cnt = 0
for num in numbers:
    # 팀이 이루어진 상태이므로 다음 팀의 최소 인원 수의 제한을 갱신
    if cnt == 0:
        limit = num
    cnt += 1 # 팀원 증가
    # 팀이 이루어 진다.
    if cnt == limit:
        cnt = 0 # 갱신
        result += 1

# 팀원이 남아있는 경우 팀 증가
if cnt > 0:
    result += 1
print(result)

