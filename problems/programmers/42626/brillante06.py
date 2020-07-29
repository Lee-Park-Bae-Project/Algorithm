import heapq


def solution(scoville, K):
    answer = 0
    sco = []
    for s in scoville:
        heapq.heappush(sco, s)
    while True:
        if sco[0] >= K:
            break
        if len(sco) == 1:
            break
        a = heapq.heappop(sco)
        b = heapq.heappop(sco)
        heapq.heappush(sco, (a+b*2))
        answer += 1
    if len(sco) == 1 and sco[0] < K:
        return -1

    return answer
