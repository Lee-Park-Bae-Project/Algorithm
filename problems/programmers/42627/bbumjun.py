import heapq


def solution(jobs):
    answer = 0
    n = len(jobs)
    jobs.sort(key=lambda item: item[0], reverse=True)
    time = 0
    q = []
    while len(jobs) != 0 or len(q) != 0:
        while len(jobs) != 0:

            if jobs[-1][0] > time:
                break
            work = jobs.pop()
            heapq.heappush(q, (work[1], work[0]))
        if len(q) != 0:
            worked = heapq.heappop(q)
            answer += (time-worked[1]) + worked[0]
            time += worked[0]
        else:
            time += 1

    return answer//n
