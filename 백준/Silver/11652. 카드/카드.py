N = int(input())
state = {}
for _ in range(N):
    number = int(input())
    if number not in state:
        state[number] = 1
    else:
        state[number] += 1
result = sorted(state.items(), key=lambda x:(-x[1], x[0]))
print(result[0][0])
