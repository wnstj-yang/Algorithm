# Baekjoon Online Judge - 2503번. 숫자 야구
N = int(input())
result = 0
num_list = []
cnt = 0
for _ in range(N):
    target, s, b = map(int, input().split())
    target = str(target)
    # 123 <= number < 1000
    for number in range(123, 1000):
        # 1의 자리가 0이면 X
        if number % 10 == 0:
            if number not in num_list:
                num_list.append(number)
            continue
        # 10의 자리가 0이면 X
        if (number // 10) % 10 == 0:
            if number not in num_list:
                num_list.append(number)
            continue
        number = str(number)
        # 서로 다른 수이므로 각 자리의 수가 1개 초과인 경우 X
        if number.count(number[0]) > 1 or number.count(number[1]) > 1 or number.count(number[2]) > 1:
            if number not in num_list:
                num_list.append(number)
            continue
        cnt_s, cnt_b = 0, 0
        for j in range(3):
            # 스트라이크인 경우
            if number[j] == target[j]:
                cnt_s += 1
            # 볼인 경우
            elif number[j] in target:
                cnt_b += 1
        # 주어진 스트라이크, 볼의 수랑 맞지 않는 경우 가능성 X인 숫자임
        if cnt_s != s or cnt_b != b:
            if number not in num_list:
                num_list.append(number)
print(1000-123-len(num_list))
