n, h = map(int, input().split())
top = []
bottom = []
for i in range(n):
    if i % 2 == 0:
        bottom.append(int(input()))
    else:
        top.append(int(input()))
top.sort()
bottom.sort()
obstacles = []
for i in range(1, h+1):
    l, r = 0, len(bottom)-1
    bottomCnt = 0
    while l <= r:
        mid = (l+r)//2
        if bottom[mid] >= i:
            bottomCnt = len(bottom) - mid
            r = mid - 1
        else:
            l = mid + 1

    topCnt = 0
    l, r = 0, len(top)-1
    while l <= r:
        mid = (l+r)//2
        if h - top[mid] < i:
            topCnt = len(top) - mid
            r = mid - 1
        else:
            l = mid + 1
    obstacles.append(topCnt+bottomCnt)
res = min(obstacles)
print(res, obstacles.count(res))
