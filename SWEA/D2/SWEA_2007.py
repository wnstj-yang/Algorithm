# SW Expert Academy - 2007번. 패턴 마디의 길이

T = int(input())

for tc in range(1, T + 1):
    string = input()
    result = 0
    # 패턴을 숫자가 낮은 것 부터 높은 것까지 가면 중복이 더 될 수 있는 문제가 있어서 뒤에서부터 비교
    for i in range(10, 0, -1):
        if string[:i] == string[i:i*2]:
            result = i
    print('#{} {}'.format(tc, result))
