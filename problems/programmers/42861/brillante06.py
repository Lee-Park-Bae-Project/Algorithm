def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    visited = [0] * n
    visited[0] = 1
    while sum(visited) != n:
        for cost in costs:
            x, y, val = cost[0], cost[1], cost[2]
            if visited[x] and visited[y]:
                continue
            if visited[x] or visited[y]:
                visited[x] = 1
                visited[y] = 1
                answer += val
                break
    return answer
