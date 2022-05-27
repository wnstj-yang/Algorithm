# Baekjoon Online Judge - 1475번. 방 번호

numbers = list(map(int, input()))
cnt = 0
N = len(numbers)
result = -1 * N # 세트로 만들어진 수 만큼 -1을 곱해서 추후에 이 값과 같다면 끝난것으로 판단
while True:
    nums = list(range(0, 10))
    cnt += 1
    for i in range(N):
        if numbers[i] == -1:
            continue
        # 세트로 만들어진 수들 중 안쓰여져있을 시 numbers의 수를 -1로 갱신
        if nums[numbers[i]] != -1:
            nums[numbers[i]] = -1
            numbers[i] = -1
        else:
            # 쓰여져 있는 경우에서 6이나 9일 경우 각각에 대한 조건 처리
            if numbers[i] == 6:
                if nums[9] != -1:
                    nums[9] = -1
                    numbers[i] = -1
            elif numbers[i] == 9:
                if nums[6] != -1:
                    nums[6] = -1
                    numbers[i] = -1
        # 세트로 만들어진 수가 -10이라는 것이 세트의 수를 모두 썼기 때문에 끝
        if sum(nums) == -10:
            break
    if sum(numbers) == result:
        print(cnt)
        break

