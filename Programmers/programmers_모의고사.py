def solution(answers):
    answer = []
    result = [0] * 4
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    f_len, s_len, t_len = len(first), len(second), len(third)
    for i in range(len(answers)):
        if answers[i] == first[i % f_len]:
            result[1] += 1
        if answers[i] == second[i % s_len]:
            result[2] += 1
        if answers[i] == third[i % t_len]:
            result[3] += 1
    max_val = max(result)
    for i in range(1, 4):
        if max_val == result[i]:
            answer.append(i)

    return answer