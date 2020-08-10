import heapq


def solution(operations):
    answer = []
    res = []
    for i in range(len(operations)):
        if operations[i][0] == "I":
            heapq.heappush(res, int(operations[i][2:]))
        if operations[i][0] == "D":
            if len(res) == 0:
                continue
            if operations[i][2] == "-":
                a = heapq.heappop(res)
            else:
                heapq._heapify_max(res)
                t = heapq._heappop_max(res)
                heapq.heapify(res)
    if len(res) >= 2:
        heapq._heapify_max(res)
        t = heapq._heappop_max(res)
        answer.append(t)
        heapq.heapify(res)
        answer.append(heapq.heappop(res))
    elif len(res) == 1:
        t = heapq.heapop(res)
        answer.extend((t, t))
    else:
        answer.extend((0, 0))

    return answer
