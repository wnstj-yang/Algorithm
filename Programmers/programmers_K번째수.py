def solution(array, commands):
    answer = []
    for item in commands:
        i, j, k = item[0], item[1], item[2]
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer