# Baekjoon Online Judge - 10798번. 세로읽기

words = [list(input()) for _ in range(5)]
max_len = 0
answer = ''
for i in range(5):
    length = len(words[i])
    # 각 단어의 최대 길이를 구해서 나중에 어느정도까지 할지 판단이 가능하다
    if length > max_len:
        max_len = length
    # 최대가 15이므로 각 단어의 길이만큼 빼서 공백 부분을 채워넣어준다
    words[i] += [''] * (15 - length)

for i in range(max_len):
    for j in range(5):
        if words[j][i] != '':
            answer += words[j][i]
print(answer)
