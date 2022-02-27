# Baekjoon Online Judge - 2447번. 별 찍기 - 10


def getStars(arr):
    temp = []
    star_len = len(arr)
    for i in range(3 * star_len):
        # 중간 부분을 따로 처리해준다. 비어있게
        if i // star_len == 1:
            temp.append(arr[i % star_len] + ' ' * star_len + arr[i % star_len])
        # 3제곱으로 증가
        else:
            temp.append(arr[i % star_len] * 3)
    return temp


N = int(input())

stars = ['***', '* *', '***']
cnt = 0
# 횟수
while N != 3:
    N = N // 3
    cnt += 1

for _ in range(cnt):
    # 횟수마다 3의 거듭제곱이므로 초기화를 계속 해줌
    stars = getStars(stars)

for i in stars:
    print(i)
