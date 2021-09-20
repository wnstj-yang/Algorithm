def solution(numbers, target):
    answer = 0
    length = len(numbers)
    result = 0
    def check(cnt, result):
        # nonlocal : 지역변수가 아님을 뜻하며
        # 함수 바로 한단계 바깥쪽과 변수 바인딩 가능하다
        nonlocal answer
        if cnt == length:
            if result == target:
                answer += 1
            return
        # numbers안의 값을 재귀로 더하면서 빼는 형태로 이어나간다
        check(cnt+1, result+numbers[cnt])
        check(cnt+1, result-numbers[cnt])

    check(0, 0)
    return answer