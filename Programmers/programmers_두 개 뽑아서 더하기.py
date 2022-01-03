def solution(numbers):
    answer = []
    # 두 개의 수를 뽑아서 진행하므로 numbers안의 첫 인덱스부터 하나씩 뽑아나간다
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            num = numbers[i] + numbers[j]
            # 이미 존재한다면 다시 추가할 필요는 없다.
            if num not in answer:
                answer.append(num)
    # 만들어진 리스트를 오름차순으로 정렬
    answer.sort()
    return answer