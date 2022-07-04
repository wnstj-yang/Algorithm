def solution(files):
    answer = []
    result = []
    for file in files:
        head, number, tail = '', '', ''
        n_check = False
        for i in range(len(file)):
            # 숫자일 때 별도의 flag인 n_check를 둬서 number임을 알린다.
            if file[i].isdigit():
                number += file[i]
                n_check = True
            # number가 아닌 경우에는 head를 뜻하고, 이게 아닐 경우 아래의 tail임을 말한다
            elif not n_check:
                head += file[i]
            else:
                tail = file[i:]
                break
        # 추후에 영대소문자 구분이 없기 때문에 미리 대문자로 만들어진 형태의 head를 추가
        result.append((head, head.upper(), number, tail))
    # 나열된 파일들의 정보로 정렬
    result.sort(key=lambda x: (x[1], int(x[2])))

    for file in result:
        answer.append(''.join(file[0] + file[2] + file[3]))

    return answer
