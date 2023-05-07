def solution(t, p):
    answer = 0
    len_p = len(p) # p 의 길이
    # t의 길이에서 p의 길이를 뺀 것만큼(인덱스상 + 1추가) 반복을 진행
    for i in range(len(t) - len_p + 1):
        # a : 반복하면서 i의 인덱스부터 p의 길이만큼의 수 / b : p의 수
        a, b = int(t[i:i+len_p]), int(p)
        if a <= b: # a가 b보다 작거나 같다면 경우의 수 1추가
            answer += 1
    return answer
