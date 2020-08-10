from collections import deque


def solution(n, edge):
    answer = 0
    ans = []
    res = []
    checked = [[]*(n+1) for _ in range(n+1)]
    visited = [-1 for _ in range(n+1)]
    for e in edge:
        dX, dY = e[0], e[1]
        checked[dX].append(dY)
        checked[dY].append(dX)
    cnt = 0
    que = deque([[1, cnt]])
    while que:
        t = que.popleft()
        temp = t[1]
        if visited[t[0]] == -1:
            visited[t[0]] = t[1]
            temp += 1
            for i in checked[t[0]]:
                que.append([i, temp])

    val = max(visited)
    for i in range(len(visited)):
        if visited[i] == val:
            answer += 1
    return answer
