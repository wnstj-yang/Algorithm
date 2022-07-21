# Baekjoon Online Judge - 1350번. 진짜 공간

N = int(input())
files = list(map(int, input().split()))
cluster = int(input())
disk = 0
for file in files:
    # 파일 크기가 0 이면 클러스터 필요 X 
    if file == 0:
        continue
    # 파일 크기가 클러스터 크기만큼 나눈 값으로 클러스터 크기 만큼 곱한다.
    if file // cluster:
        result = cluster * (file // cluster)
        disk += cluster * (file // cluster)
        # 이후 나머지의 값이 존재한다면 cluster크기만큼 더 필요하므로 disk 크기에 추가
        if (file - result) % cluster:
            disk += cluster
    # 파일 크기가 클러스터 크기 보다 작은 경우 해당 클러스터 크기 만큼 더해준다
    else:
        disk += cluster
print(disk)
