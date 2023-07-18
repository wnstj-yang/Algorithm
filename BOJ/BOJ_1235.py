# Baekjoon Online Judge - 1235번. 학생 번호


N = int(input())
stu_nums = []
for _ in range(N):
    stu_nums.append(input())
k = len(stu_nums[0]) # 문자열 길이가 다 같기 때문에 첫번째로 구한다
for i in range(1, k + 1):
    found = True # 디폴트로
    num_list = [] # 각 number들의 마지막에서부터 k길이만큼 값을 넣는다
    for number in stu_nums:
        # 같은 값이 존재한다면 찾지못했다는 flag인 found를 false 처리
        # 그렇지 않다면 리스트에 추가한다
        if number[-i:] in num_list:
            found = False
            break
        else:
            num_list.append(number[-i:])
    if found:
        print(i)
        break
