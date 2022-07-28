# Baekjoon Online Judge - 1408번. 24

now = input()
target = input()
# 모두 second(초)로 환산해서 남은 시간을 구한 뒤 다시 시, 분, 초로 출력한다
now_time = int(now[:2]) * 3600 + int(now[3:5]) * 60 + int(now[6:])
target_time = int(target[:2]) * 3600 + int(target[3:5]) * 60 + int(target[6:])
left_time = target_time - now_time
# 현재 시간이 임수 시간보다 큰 경우 다음 날까지를 포함해야 되기 때문에 24시간을 초로 추가한다
if now_time > target_time:
    left_time += 24 * 3600
hour = left_time // 3600
left_time = left_time % 3600
minute = left_time // 60
left_time = left_time % 60
second = left_time
result = ''

if hour < 10:
    result += '0' + str(hour)
else:
    result += str(hour)
result += ':'
if minute < 10:
    result += '0' + str(minute)
else:
    result += str(minute)
result += ':'
if second < 10:
    result += '0' + str(second)
else:
    result += str(second)
print(result)
