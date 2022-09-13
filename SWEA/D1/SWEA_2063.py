# SW Expert Academy - 2063번. 중간값 찾기


N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
print(numbers[len(numbers) // 2])
