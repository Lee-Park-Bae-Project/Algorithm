def getParent(parent, x):
    if parent[x] == x:
        return x
    return getParent(parent, parent[x])


def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a == b:
        return True
    else:
        return False


def solution(n, costs):
    answer = 0
    nodes = sorted(costs, key=lambda item: item[2])
    parents = [i for i in range(n)]
    for node in nodes:
        a, b, cost = tuple(node)
        if findParent(parents, a, b) == False:
            unionParent(parents, a, b)
            answer += cost

    return answer
