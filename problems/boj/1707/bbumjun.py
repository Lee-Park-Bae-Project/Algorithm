from collections import deque


def bfs(node, f):
    global ans, graph, isVisit
    q = deque([(node, f)])
    isVisit[node] = (True, 1)
    while len(q) != 0:
        cur, flag = q.popleft()
        for nxt in graph[cur]:
            if isVisit[nxt][0] == True:
                if isVisit[nxt][1] == flag:
                    ans = 'NO'
                    return
            else:
                isVisit[nxt] = (True, flag * -1)
                q.append((nxt, flag*-1))


tc = int(input())
for _ in range(tc):
    n, e = map(int, input().split())
    graph = {}
    for i in range(e):
        a, b = map(int, input().split())
        graph.setdefault(a, {})
        graph.setdefault(b, {})
        graph[a].setdefault(b, {})
        graph[b].setdefault(a, {})
    isVisit = [(False, 0) for _ in range(n+1)]
    ans = 'YES'
    for i in graph:
        if isVisit[i][0] == True:
            continue
        bfs(i, 1)
        if ans == 'NO':
            break

    print(ans)
