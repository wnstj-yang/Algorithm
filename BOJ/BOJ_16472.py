# Baekjoon Online Judge - 16472번. 고냥이

N = int(input())
string = input()
str_list = []
l, r = 0, 1
set_list = set(string[l])
result = 0
# 문자열이 1개이면 1로 출력
if len(string) == 1:
    print(1)
# 문자열에서의 알파벳 수가 알파벳 종류 수보다 같거나 작으면 문자열 길이만큼이 정답이다.
elif len(set(string)) <= N:
    print(len(string))

else:
    # 투 포인터를 활용해서 길이를 체크한다.
    while l < len(string) and r < len(string):
        set_list.add(string[r])
        # N개 종류의 알파벳이 존재한다면 문자열의 길이를 r - l + 1로 정한다. 1를 더한 이유는 인덱스를 기준으로 빼기 때문임
        if len(set_list) == N:
            result = max(result, r - l + 1)
            r += 1 # 추가적으로 더 늘려서 진행
        # N개 보다 큰 경우라면 현재까지의 set으로 된 알파벳 개수를 초기화를 진행한다.
        # 진행한 이후 l과 r또한 위치를 초기화 진행
        elif len(set_list) > N:
            set_list = set()
            l += 1
            set_list.add(string[l])
            r = l + 1
        else:
            r += 1
    print(result)

