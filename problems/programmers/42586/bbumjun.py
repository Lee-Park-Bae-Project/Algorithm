def solution(progresses, speeds):
    answer = []
    time = 0
    while len(progresses) > 0:
        time += 1
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        completed = 0
        while len(progresses) > 0:
            if progresses[0] >= 100:
                completed += 1
                progresses.pop(0)
                speeds.pop(0)
            else:
                break
        if completed != 0:
            answer.append(completed)
    return answer


print(solution([93, 30, 55], [1, 30, 5]	))
