# Baekjoon Online Judge - 10988번. 팰린드롬인지 확인하기

string = input()

answer = 1
idx = 0
while idx < len(string) // 2:
    if string[idx] != string[-idx-1]:
        answer = 0
        break
    idx += 1
print(answer)
