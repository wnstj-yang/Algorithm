# Baekjoon Online Judge - 1339번. 단어 수학

N = int(input())
string_list = []
alpha_list = {}
result = 0
for _ in range(N):
    string_list.append(input())

# 그리디 형태인데, 각 자릿수에 대한 값을 통해 정렬을 진행한다.
for string in string_list:
    length = len(string) - 1
    for alpha in string:
        if alpha not in alpha_list:
            alpha_list[alpha] = 10 ** length
        else:
            alpha_list[alpha] += (10 ** length)
        length -= 1
num_list = []
# 각 문자열에 속한 알파벳들에서 자릿수 만큼의 값을 구한다.
# Ex) GCF인 경우, G = 100, C = 10, F = 1 / GGC인 경우, G = 100, G = 10, C = 1
# 그러면 총 G = 210, C = 11, F = 1이여서 G에는 9, C에는 8, F는 7로 놓고 각각 곱해준다. 그러면 최댓값
# GCF와 GGC에서 G는 900 + 900 + 90 = 9*(210)과 동일
for value in alpha_list.values():
    num_list.append(value)
num_list.sort(reverse=True)
number = 9

for i in num_list:
    result += (number * i)
    number -= 1
print(result)
