# Baekjoon Online Judge - 17609번. 회문
# 투 포인터 O(N)


def check(x, y):
    while x < y:
        # 같지 않다면 유사회문도 아님
        if word[x] != word[y]:
            return False
        else:
            x += 1
            y -= 1
    return True


def palindrome(s, e):
    while s < e:
        if word[s] != word[e]:
            # 같지않은 부분부터 유사회문인지 check시작
            left = check(s + 1, e)
            right = check(s, e - 1)
            # 둘 중 하나라도 True이면 해당 인덱스를 지웠을 때
            # 유사회문임을 의미하여서 1을 반환
            if left or right:
                return 1
            # 모두 False인 경우 회문, 유사회문 X
            else:
                return 2
        else:
            s += 1
            e -= 1
    # 회문이 맞다면 끝
    return 0


T = int(input())

for _ in range(T):
    word = input()
    s, e = 0, len(word) - 1
    ans = palindrome(s, e)
    print(ans)
