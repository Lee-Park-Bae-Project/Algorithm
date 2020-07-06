n, m = map(int, input().split())
trees = list(map(int, input().split()))
minH = 0
maxH = max(trees)
ans = 0
while minH <= maxH:
    cutH = (minH+maxH)//2
    cutMount = 0
    for tree in trees:
        cutMount += (tree - cutH if tree >= cutH else 0)
    if cutMount >= m:
        ans = cutH
        minH = cutH + 1
    else:
        maxH = cutH-1
print(ans)
