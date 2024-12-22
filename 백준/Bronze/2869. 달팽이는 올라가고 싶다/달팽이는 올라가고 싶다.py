A, B, V = map(int,input().split())

x=(V-B)/(A-B)

  
print(int(x) if x == int(x) else int(x)+1) 


