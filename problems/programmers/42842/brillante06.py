import math


def solution(brown, yellow):
    answer = []
    i = 1
    q = 0
    k = int(math.sqrt(brown+yellow))
    if (k*k == (brown+yellow)):
        answer.append(k)
        answer.append(k)
        return answer
    while True:
        flag = False
        for t in range(1, i+1):
            if t*i == yellow and (i+2)*(t+2) == (brown+yellow):
                answer.append(i+2)
                answer.append(t+2)
                flag = True
                break
        if flag == True:
            break
        i += 1
    return answer
