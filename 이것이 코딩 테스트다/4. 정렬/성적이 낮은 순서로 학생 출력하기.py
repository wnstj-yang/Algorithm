# 이것이 코딩 테스트다 - 4장 정렬 실전문제 3. 성적이 낮은 순서로 학생 출력하기 180p

N = int(input())
info = []
for _ in range(N):
    name, score = map(str, input().split())
    info.append((int(score), name))
info.sort(key=lambda x:x[0])
for score, name in info:
    print(name, end=' ')

# 2
# 홍길동 95
# 이순신 77
