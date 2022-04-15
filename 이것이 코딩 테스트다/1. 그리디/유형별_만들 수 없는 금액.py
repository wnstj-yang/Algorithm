# 유형별 문제 4. 만들 수 없는 금액 - 314p

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort() # 만들 수 없는 양의 정수 중 최소값이므로 오름차순 정렬 진행
answer = 1 # 최솟값 1부터 시작해서 정렬된 숫자들과 더하면서 값을 구한다.
# Ex) 1 1 8이라고 했을 때 1) 1 + 1, 2) 2 + 1, 3) 3은 8보다 작으므로 이 것이 최종 답으로 판단한다. 만약 8이 아니라 3이라면
# 3 + 3해서 6이 답이된다.
for num in numbers:
    if answer < num:
        break
    answer += num
print(answer)


# 입력 - 1
# 5
# 3 2 1 1 9
# 출력 - 1
# 8

# 입력 - 2
# 3
# 3 5 7
# 출력 - 2
# 1

