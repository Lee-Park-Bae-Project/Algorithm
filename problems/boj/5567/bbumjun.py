from collections import deque
n = int(input())
m = int(input())
relation = {}

for i in range(m):
    a, b = map(int, input().split())
    relation.setdefault(a, {})
    relation.setdefault(b, {})
    relation[a].setdefault(b, {})
    relation[b].setdefault(a, {})
ans = set([])
q = deque([(1, 0)])
isVisit = [False for _ in range(n+1)]

while len(q) != 0:
    cur, dist = q.popleft()
    ans.add(cur)
    if dist == 2:
        continue
    for x in relation[cur]:
        if isVisit[x] == True or relation.get(x, False) == False:
            continue
        q.append((x, dist+1))

print(len(ans)-1 if len(ans) > 0 else 0)
