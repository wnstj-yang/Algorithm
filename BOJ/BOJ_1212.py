# Baekjoon Online Judge - 1212번. 8진수 2진수

num = input()
ans = bin(int(num, 8))
# ans : 0bxxxxxxx
print(ans[2:])