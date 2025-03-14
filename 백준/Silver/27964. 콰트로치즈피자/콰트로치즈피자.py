N = int(input())
topping_list = list(map(str, input().split()))
toppings = {}
target = "Cheese"

for topping in topping_list:
    if len(topping) >= len(target):
        if topping[-len(target):] == target:
            if topping not in toppings:
                toppings[topping] = 1
            else:
                toppings[topping] += 1

if len(toppings) >= 4:
    print('yummy')
else:
    print('sad')
