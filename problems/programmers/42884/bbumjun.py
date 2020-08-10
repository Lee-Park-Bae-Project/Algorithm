def solution(routes):
    answer = 1
    routes.sort()
    minX = 30001
    for route in routes:
        if route[0] > minX:
            answer += 1
            minX = route[1]
        elif route[1] < minX:
            minX = route[1]
    return answer
