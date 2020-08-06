import queue


def bfs(n, graph):
    q = queue.Queue()
    isVisit = [False for _ in range(n+1)]
    q.put((1, 0))
    isVisit[1] = True
    result = {}
    while q.empty() != True:
        cur, cost = q.get()
        for nextNode in graph[cur]:
            if isVisit[nextNode] == True:
                continue
            isVisit[nextNode] = True
            result[cost+1] = result.get(cost+1, 0) + 1
            q.put((nextNode, cost+1))
    return result[cost]


def solution(n, edge):
    answer = 0
    graph = {}
    for e in edge:
        graph.setdefault(e[0], [])
        graph.setdefault(e[1], [])
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    answer = bfs(n, graph)
    return answer
