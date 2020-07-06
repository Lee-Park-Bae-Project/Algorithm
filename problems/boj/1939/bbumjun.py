n, m = map(int, input().split())
# islands = [[0 for _ in range(n+1)] for _ in range(n+1)]
islands = {}
maxW = 0
for i in range(m):
    r, c, w = map(int, input().split())
    islands.setdefault(r, {})
    if islands[r].get(c, 0) < w:
        islands[r][c] = w
    islands.setdefault(c, {})
    if islands[c].get(c, 0) < w:
        islands[c][r] = w
    if maxW < w:
        maxW = w
start, end = map(int, input().split())


def bfs(mid):
    global ans, islands, start, end
    isVisit = [False for _ in range(n+1)]
    queue = [start]
    while len(queue) != 0:
        pos = queue.pop(0)
        if pos == end:
            return True
        for i in islands[pos]:
            if isVisit[i] == True or islands[pos][i] < mid:
                continue
            isVisit[i] = True
            queue.append(i)
    return False


ans = 0
l, r = 1, maxW
while l <= r:
    mid = (l+r) // 2
    if bfs(mid) is True:
        ans = mid
        l = mid+1
    else:
        r = mid - 1

print(ans)
