# Baekjoon Online Judge - 20291번. 파일 정리

file_list = {}
N = int(input())
for _ in range(N):
    item = input()
    # ' . '이 있는 인덱스부터 끝까지 확장자를 구하고
    extension = item[item.index('.')+1:]
    # 없는 확장자이면 개수 cnt
    if extension not in file_list:
        file_list[extension] = 1
    # 있다면 개수 증가
    else:
        file_list[extension] += 1
# key값 기준으로 정렬을 해준다
align_files = sorted(file_list.items())
for item in align_files:
    print(item[0], item[1])
