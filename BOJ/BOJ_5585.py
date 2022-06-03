# Baekjoon Online Judge - 5585번. 거스름돈

price = 1000 - int(input())
money_list = [500, 100, 50, 10, 5, 1]
result = 0
for money in money_list:
    if price >= money:
        result += price // money
        price = price % money
print(result)
