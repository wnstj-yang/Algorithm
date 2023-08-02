# Baekjoon Online Judge - 17219번. 비밀번호 찾기

N, M = map(int, input().split())
address_pw = {} # 해시
for _ in range(N):
    address, pw = map(str, input().split())
    address_pw[address] = pw
    
for _ in range(M):
    address = input()
    print(address_pw[address])
