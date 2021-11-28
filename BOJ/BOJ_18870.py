# Baekjoon Online Judge - 18870번. 좌표 압축

N = int(input())

# 받은 입력
num_list = list(map(int, input().split()))
# 중복 제거 후 정렬해서 인덱싱 처리
numbers = list(sorted(set(num_list)))
dict_numbers = {}
# 딕셔너리로 num_list의 값의 인덱스를 저장한다.
for i in range(len(numbers)):
    dict_numbers[numbers[i]] = i

# list.index의 경우 O(N)이기 때문에, 딕셔너리로 해당 값의 인덱스를 구한다.
for item in num_list:
    print(dict_numbers[item], end=' ')
