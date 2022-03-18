def solution(s):
    answer = []
    # s가 문자열로 되어있기 때문에 불필요한 부분과 숫자 집합을 split()으로 나눈다.
    s = s.replace('{{', '').replace('}}', '').split('},{')
    s.sort(key = lambda x : len(x)) # 문자 길이로 정렬을 해줘야함
    for nums in s:
        # 각 리스트에 있는 문자열 숫자 집합을 ','로 숫자들로만 이루어지게 만듬
        nums = nums.split(',')
        # 각 숫자가 중복되는지 체크
        for num in nums:
            num = int(num)
            if num not in answer:
                answer.append(num)
    return answer