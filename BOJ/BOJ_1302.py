# Baekjoon Online Judge - 1302번. 베스트셀러

N = int(input())
books = {}
for _ in range(N):
    name = input()
    if name not in books:
        books[name] = 1
    else:
        books[name] += 1
# 책의 이름이 많은 순서와 동일한게 여러 개 있다면 사전 순 정렬
books = sorted(books.items(), key=lambda x:(-x[1], x[0]))
print(books[0][0])
