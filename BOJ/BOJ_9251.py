# Baekjoon Online Judge - 9251번. LCS

first = input()
second = input()

f_len = len(first)
s_len = len(second)

arr = [[0] * (s_len + 1) for _ in range(f_len + 1)]

for i in range(1, f_len + 1):
    for j in range(1, s_len + 1):
        # 알파벳이 같을 때 알파벳 추가 전까지의 상황에서 1 추가
        if second[j - 1] == first[i - 1]:
            arr[i][j] = arr[i - 1][j - 1] + 1
        # 다르다면 행, 열 바꾸어서 최대 값을 넣는다.
        # 예시 => first : ACA, second : CAP인 경우 ACA와 CA, AC와 CAP를 비교한다.
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
print(arr[f_len][s_len])

