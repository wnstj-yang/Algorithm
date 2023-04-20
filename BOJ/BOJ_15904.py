# Baekjoon Online Judge - 15904번.  UCPC는 무엇의 약자일까?

string = input()
result = ''
idx = 0
get_string = ['U', 'C', 'P', 'C']
for i in string:
    if idx < len(get_string):
        if get_string[idx] == i:
            result += get_string[idx]
            idx += 1
    else:
        break
if len(result) == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')
