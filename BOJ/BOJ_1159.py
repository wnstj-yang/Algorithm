# Baekjoon Online Judge - 1159번. 농구 경기

N = int(input())

player_list = {}
for _ in range(N):
    player = input()
    if player[0] not in player_list:
        player_list[player[0]] = 1
    else:
        player_list[player[0]] += 1
result = ''
for key, value in player_list.items():
    if value >= 5:
        result += key
if result != '':
    result = list(result)
    result.sort()
    print(''.join(result))
else:
    print('PREDAJA')
