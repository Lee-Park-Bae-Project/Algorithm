def solution(routes):
    answer = 1
    routes.sort()
    cur = routes[0][1]
    for i in range(1, len(routes)):
        print(i)
        if cur > routes[i][1]:
            cur = routes[i][1]
        if cur < routes[i][0]:
            cur = routes[i][1]
            answer += 1
    return answer
