# Baekjoon Online Judge - 9046번. 복호화

T = int(input())
for tc in range(T):
    # 알파벳 개수 만큼 카운트된 값을 0으로 초기화
    alphabet = [0] * 26
    encrypted = input()
    # 각 암호문의 알파벳을 체크한다.
    for alpha in encrypted:
        # 알파벳이 공백이 아닐 경우
        if alpha != ' ':
            # 해당하는 알파벳의 개수를 카운트
            alphabet[ord(alpha) - 97] += 1
    # 개수가 가장 많이 나온 알파벳의 개수를 구한다.
    cnt = alphabet.count(max(alphabet))
    # 1보다 크면 복호시 판별이 어렵기 때문에 ? 으로 출력
    if cnt > 1:
        print('?')
    # 1이라면 해당 알파벳의 인덱스를 구해서 알파벳을 출력
    else:
        print(chr(alphabet.index(max(alphabet)) + 97))
