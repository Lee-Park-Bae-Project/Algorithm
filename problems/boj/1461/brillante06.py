n, m = map(int, input().split())
book, book1, book2, res, maxVal = list(
    map(int, input().split())), [], [], 0, -1
book.sort()
for b in range(n):
    if maxVal < abs(book[b]):
        maxVal = abs(book[b])
    if book[b] < 0:
        book1.append(book[b])
    else:
        book2.append(book[b])
book2.sort(reverse=True)

for i in range(0, len(book1), m):
    res += abs(book1[i]*2)
for i in range(0, len(book2), m):
    res += abs(book2[i]*2)

res -= maxVal
print(res)
