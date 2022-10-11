# SW Expert Academy - 5658번. [모의 SW 역량테스트] 보물상자 비밀번호

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(input())
    num_list = set()
    first = list(numbers[:])
    # 첫번째는 먼저 해두고 회전시킨다
    for i in range(0, N, N//4):
        num = numbers[i:i+N//4]
        num_list.add(''.join(num))
    while True:
        tmp = []
        # 회전위해 뒤에거를 빼서 앞에다 붙인다.
        number = numbers.pop()
        numbers = [number] + numbers
        # 주어진 N의 수에서 4만큼 나눈 것으로 리스트 슬라이싱
        for i in range(0, N, N//4):
            num = numbers[i:i+N//4]
            # 첫번째와 같은지 tmp 리스트에 넣는다
            tmp.extend(numbers[i:i+N//4])
            num_list.add(''.join(num))
        # 첫번째랑 같다면 끝
        if tmp == first:
            break
    # set을 list로 바꾸어주고 내림차순으로 정렬한다
    num_list = list(num_list)
    num_list.sort(reverse=True)
    # 주어진 16진수값을 10진수 정수형으로 만들어서 출력
    print('#{} {}'.format(t, int(num_list[K-1], 16)))
