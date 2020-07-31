import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if K == 0:
        return 0

    while len(scoville) > 0:
        minS = scoville[0]
        if minS >= K:
            break
        else:
            if len(scoville) < 2:
                return -1
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            if a == 0 and b == 0:
                return -1
            heapq.heappush(scoville, a+b*2)
            answer += 1

    return answer
