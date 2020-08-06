import heapq


def solution(jobs):
    answer = 0
    res = []
    start, end, cnt, done = -2, 0, 0, 0
    while len(jobs) != done:
        for i in range(len(jobs)):
            if jobs[i][0] <= end and start < jobs[i][0]:
                heapq.heappush(res, (jobs[i][1], jobs[i][0]))
        if len(res):
            temp = heapq.heappop(res)
            answer += (temp[0]+end-temp[1])
            start = end
            end += temp[0]
            done += 1
        else:
            end += 1

    return int(answer/len(jobs))
