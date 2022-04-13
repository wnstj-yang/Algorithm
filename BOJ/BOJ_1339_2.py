# Baekjoon Online Judge - 1339번. 단어 수학
# 시간 초과로 통과는 안되나 완전 탐색으로의 풀이에 대한 연습
# 사실상 어떻게 시간을 줄여야되는지 고민하다가 그리디로 인한 풀이 참고함...


def permutation(k, n, number):
    global answer
    # 입력받은 각 문자열에 값들을 곱하면서 최댓값을 구한다 => 순열에 각각 돌게되면 시간 초과 나는 이유
    if k == n:
        result = 0
        for string in string_list:
            num = 0
            for alpha in string:
                num *= 10
                num += alpha_list[alpha]
            result += num
        answer = max(answer, result)
        return
    # 순열을 통해 각 알파벳에 값을 저장
    for i in range(len(alpha_list)):
        if not visited[i]:
            visited[i] = True
            alpha_list[perm[i]] = number
            permutation(k + 1, n, number - 1)
            visited[i] = False


N = int(input())
string_list = []
alpha_list = {} # key는 알파벳, value는 값
perm = [] # 전체 알파벳들 넣음
for _ in range(N):
    string = input()
    string_list.append(string)
    for alpha in string:
        if alpha not in alpha_list:
            alpha_list[alpha] = 0
            perm.append(alpha)
answer = 0
visited = [False] * len(alpha_list)
permutation(0, len(alpha_list), 9)
print(answer)
