def solution(n, words):
    answer = [0, 0]
    # 단어들을 비교할 때 뒤에 것이 틀림을 말한다.
    for i in range(len(words) - 1):
        # 중복되는 단어일 경우 뒷 단어까지 같은 것이 있는지 확인해서 중복체크를 한다.
        if words[i][-1] != words[i + 1][0] or (words[i + 1] in words[:i + 1]):
            # 번호의 경우 나머지 연산 +1, 횟수의 경우 나누기 연산 + 1
            answer = [(i + 1) % n + 1, (i + 1) // n + 1]
            break

    return answer