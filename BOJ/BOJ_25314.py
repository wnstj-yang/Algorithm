# Baekjoon Online Judge - 25314번. 코딩은 체육과목 입니다

N = int(input())
result = []
for _ in range(N // 4):
    result.append('long')
result.append('int')
# list로 된 것을 데이터 간격에 공백으로 나누어서 처리해준다
print(' '.join(result))
