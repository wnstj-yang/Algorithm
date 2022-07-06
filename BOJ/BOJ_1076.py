# Baekjoon Online Judge - 1076번. 저항

resist = {
    'black': [0, 1], 'brown': [1, 10], 'red': [2, 100], 'orange': [3, 1000],
    'yellow': [4, 10000], 'green': [5, 100000], 'blue': [6, 1000000],
    'violet': [7, 10000000], 'grey': [8, 100000000], 'white': [9, 1000000000]
}


first = input()
second = input()
third = input()
result = ''
result += str(resist[first][0])
result += str(resist[second][0])
result = int(result)
result *= resist[third][1]
print(result)
