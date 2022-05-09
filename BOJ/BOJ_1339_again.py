# Baekjoon Online Judge - 1339번. 단어 수학

N = int(input())
string_list = []
alpha_list = {}
answer = 0
for _ in range(N):
    string_list.append(input())


for string in string_list:
    length = len(string) - 1
    # 각 단어별로 길이를 구하고 해당 알파벳이 존재유무에 따라 자릿수만큼 곱해서 더해준다
    for alpha in string:
        if alpha not in alpha_list:
            alpha_list[alpha] = 10 ** length
        else:
            alpha_list[alpha] += 10 ** length
        length -= 1

# 가장 큰 값 순서대로 정렬을 한 후 9부터 순차적으로 곱해주면서 더해나감
result = sorted(alpha_list.values(), reverse=True)
cnt = 9

for num in result:
    answer += cnt * num
    cnt -= 1
print(answer)
