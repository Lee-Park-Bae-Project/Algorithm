def solution(cacheSize, cities):
    answer = 0
    cities = list(map(lambda item: item.lower(), cities))
    q = []
    for i in range(len(cities)):
        if cities[i] in q:
            answer += 1
            q.pop(q.index(cities[i]))
            q.append(cities[i])
        else:
            answer += 5
            if cacheSize > 0:
                if len(q) >= cacheSize:
                    q.pop(0)
                q.append(cities[i])

    return answer
