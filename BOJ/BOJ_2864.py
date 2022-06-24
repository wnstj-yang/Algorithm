# Baekjoon Online Judge - 2864번. 5와 6의 차이


A, B = map(str, input().split())
min_val = int(A.replace('6', '5')) + int(B.replace('6', '5'))
max_val = int(A.replace('5', '6')) + int(B.replace('5', '6'))
print(min_val, max_val)

