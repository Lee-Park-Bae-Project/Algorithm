from collections import deque
n = int(input())
a, b = map(int, input().split())
m = int(input())
relation = {}
for i in range(m):
    parent, child = map(int, input().split())
    relation.setdefault(parent, {})
    relation.setdefault(child, {})
    relation[parent].setdefault(child, {})
    relation[child].setdefault(parent, {})
ans = -1


def bfs(x, y):
    global relation, ans
    isVisit = [False for _ in range(n+1)]
    queue = deque([(x, 0)])
    while len(queue) != 0:
        cur, cost = queue.popleft()
        if cur == y:
            ans = cost
            return
        for child in relation[cur]:
            if isVisit[child] == True or relation.get(child, 0) == 0:
                continue
            isVisit[child] = True
            queue.append((child, cost+1))


bfs(a, b)
print(ans)
