# Baekjoon Online Judge - 2083번. 럭비 클럽


while True:
    name, age, weight = map(str, input().split())
    if name == '#':
        break
    age = int(age)
    weight = int(weight)
    if age > 17 or weight >= 80:
        print(name, 'Senior')
    else:
        print(name, 'Junior')
