n, m = map(int, input().split())
homes = []
for i in range(n):
    homes.append(int(input()))
homes.sort()
minGap = 1
maxGap = homes[-1]-homes[0]
ans = 0
if m < 3:
    ans = maxGap
else:
    while minGap <= maxGap:
        middle = (minGap + maxGap) // 2
        cnt = m-2
        point = homes[0]
        for i in range(1, len(homes)-1):
            if homes[i] - point >= middle and homes[-1] - homes[i] >= middle:
                cnt -= 1
                point = homes[i]
            if cnt <= 0:
                ans = middle
                minGap = middle+1
                break
        else:
            maxGap = middle - 1
print(ans)
