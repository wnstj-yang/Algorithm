# Baekjoon Online Judge - 4358번. 생태학
import sys

input = sys.stdin.readline

tree_list = {}
total = 0
while True:
    # 오른쪽 공백제거 입력받는다
    tree = input().rstrip()
    if tree == '':
        break

    total += 1
    if tree not in tree_list:
        tree_list[tree] = 1
    else:
        tree_list[tree] += 1

tree_list = sorted(tree_list.items())
for tree, cnt in tree_list:
    result = (cnt / total) * 100
    result_int = int(result)
    # round내장함수의 경우 짝수와 홀수일 때 올림과 내림이 다르다.
    # 그래서 format함수를 활용해서 아래와 같이 할 경우 소수자리 5번째에서 반올림을 해준다
    print("{} {:.4f}".format(tree, result))
