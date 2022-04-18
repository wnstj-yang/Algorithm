# Baekjoon Online Judge- 2437번. 저울

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
count = 1 # 양의 정수 중 최소값
# 무게의 합을 더하면서 조합적인 부분을 그리디형태로 해결
# 예를 들어 [1, 1, 2]이 있을 때 만들 수 있는 수는 [1, 2, 3, 4]이다. 무게를 더하는 변수가 count라 했을 때
# count - 1까지의 수의 조합을 만들 수 있다. 그래서 답은 양의 정수 중 최소값이므로 6이 된다.
# 그러나 15를 여기에 추가했을 때 추가적으로 만들 수 있는 수는 [1, 2, 3, 4]에 15를 더해서 [16, 17, 18, 19]이다.
# 우리는 양의 정수 중 최소값을 구해야 하므로 답은 7이 되어야한다. 그래서 현재까지 무게를 더한 값보다 큰 값이 존재하면 끝으로 판단한다.
for num in numbers:
    if count < num:
        break
    count += num
print(count)
