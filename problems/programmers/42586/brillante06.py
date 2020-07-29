import math


def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        progresses[i] = math.ceil((100-progresses[i])/speeds[i])
    fst = progresses[0]
    total = 1
    for i in range(1, len(progresses)):
        if fst < progresses[i]:
            fst = progresses[i]
            answer.append(total)
            total = 1
        else:
            total += 1

    answer.append(total)
    return answer
