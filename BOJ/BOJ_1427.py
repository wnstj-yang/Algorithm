# Baekjoon Online Judge - 1427번. 소트인사이드

N = list(map(int, input()))
result = []
while N:
    # 최대값을 구하고 넣어주면서 해당 값은 사용했으므로 제거
    max_num = max(N)
    N.remove(max_num)
    result.append(str(max_num))
print(''.join(result))

