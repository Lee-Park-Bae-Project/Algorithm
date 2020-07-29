def solution(arrangement):
    answer = 0
    res = []
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            res.append(arrangement[i])
        else:
            res.pop()
            if arrangement[i-1] == '(':
                answer += len(res)
            else:
                answer += 1
    return answer
