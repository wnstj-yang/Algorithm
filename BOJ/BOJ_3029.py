# Baekjoon Online Judge - 3029번. 경고

now = input()  # 현재 시간
throw = input()  # 나트륨 던질 시간

# 각각 문자열로된 숫자들을 숫자로 만들어준다
now_h = int(now[0]) * 10 + int(now[1])
throw_h = int(throw[0]) * 10 + int(throw[1])
now_m = int(now[3]) * 10 + int(now[4])
throw_m = int(throw[3]) * 10 + int(throw[4])
now_s = int(now[6]) * 10 + int(now[7])
throw_s = int(throw[6]) * 10 + int(throw[7])

# 정답이 되는 h(시), m(분), s(초)
ans_h, ans_m, ans_s = 0, 0, 0

# 현재 초가 나트륨 던지는 초보다 큰 경우
if now_s > throw_s:
    ans_s = 60 - now_s + throw_s
    # 분 증가
    now_m += 1
    # 시 와 분이 각각 범위 벗어나는 경우 check
    if now_m == 60:
        now_h += 1
        if now_h == 24:
            now_h = 0
        now_m = 0
else:
    ans_s = throw_s - now_s

# 현재 분이 나트륨 던지는 분보다 큰 경우
if now_m > throw_m:
    ans_m = 60 - now_m + throw_m
    now_h += 1
    # 시와 분이 각각 범위 벗어나는 경우 check 및 초기화
    if now_h == 24:
        now_h = 0
        now_m = 0
else:
    ans_m = throw_m - now_m

# 현재 시가 나트륨 던지는 시보다 큰 경우
if now_h > throw_h:
    ans_h = 24 - now_h + throw_h
else:
    ans_h = throw_h - now_h

# 이제 다시 문자열로 바꾸는 과정에서 시, 분, 초가 10보다 작은경우 앞에 0을 추가함
if ans_h < 10:
    ans_h = '0' + str(ans_h)
else:
    ans_h = str(ans_h)
if ans_m < 10:
    ans_m = '0' + str(ans_m)
else:
    ans_m = str(ans_m)
if ans_s < 10:
    ans_s = '0' + str(ans_s)
else:
    ans_s = str(ans_s)

# 예외적으로 시간이 같은 경우 하루를 기다려야 하므로 예외 처리
if ans_h == '00' and ans_m == '00' and ans_s == '00':
    ans_h, ans_m, ans_s = '24', '00', '00'

print(ans_h + ':' + ans_m + ':' + ans_s)
