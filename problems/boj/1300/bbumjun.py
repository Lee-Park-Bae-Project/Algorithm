n = int(input())
k = int(input())

minX = 1
maxX = n*n
ans = 0
while minX <= maxX:
    midX = (minX + maxX) // 2
    cnt = 0
    for i in range(1, n+1):
        cnt += min([midX//i, n])
    if cnt >= k:
        ans = midX
        maxX = midX - 1
    else:
        minX = midX + 1
print(ans)
