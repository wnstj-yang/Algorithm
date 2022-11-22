# SW Expert Academy - 4676번. 늘어지는 소리 만들기

T = int(input())

for tc in range(1, T + 1):
    word = input()
    H = int(input())
    nums = list(map(int, input().split()))
    cnt = [0] * (len(word) + 1) # 문자열 길이만큼
    result = ''
    for num in nums:
        cnt[num] += 1

    for i in range(len(word)):
        if cnt[i] == 0:
            result += word[i]
        else:
            result += ('-' * cnt[i] + word[i])
    result += '-' * cnt[-1]
    print('#{} {}'.format(tc, result))


