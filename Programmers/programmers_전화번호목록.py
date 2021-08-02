def solution(phone_book):
    answer = True
    # 길이만큼 정렬하지 않는 이유는 접두어를 비교해야하기 때문
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # 정렬이 되어있으니 현재 값 보다 다음 값의 길이가 커야함(전화번호 중복 X)
        if len(phone_book[i]) < len(phone_book[i+1]):
            # 접두어를 비교해야하니 인덱스 슬라이싱해서 다음 값의 현재 자리 길이만큼 살펴본다
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                answer = False
                break
    return answer