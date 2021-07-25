# Baekjoon Online Judge - 1316번. 그룹 단어 체커

N = int(input())
ans = 0
for _ in range(N):
    word = input()
    length = len(word)
    for i in range(length):
        # 단어의 알파벳 앞뒤를 체크
        if i != length - 1:
            # 현재 위치의 알파벳이 다음과 같다면 넘어간다.
            if word[i] == word[i+1]:
                continue
            # 다르다면 해당 알파벳이 그 다음 알파벳부터 끝까지 존재하는지 확인 / 없으면 pass
            elif word[i] in word[i+1:]:
                break
        # 단어의 끝까지 왔다면 그룹 단어이므로 단어 수 + 1
        else:
            ans += 1
print(ans)
