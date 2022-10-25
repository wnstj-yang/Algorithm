# SW Expert Academy - 9700번. USB 꽂기의 미스터리

T = int(input())

for tc in range(1, T + 1):
    p, q = map(float, input().split())
    s1 = (1 - p) * q # 1번 뒤집었을 때 ( 올바르지 않아 뒤집어서 올바른 면으로 만들고 정상적으로 꽂힘)
    s2 = p * (1 - q) * q # 2번 뒤집었을 때( 올바르게 꽂았으나 1 - q 확률로 꽂히지 않음 => 1번 뒤집었는데 뒤집어지면 절대로 안 꽂힘
    # 그래서 한 번 더 뒤집었더니 정상적으로 꽂힘
    if s1 < s2:
        print('#{} YES'.format(tc))
    else:
        print('#{} NO'.format(tc))
