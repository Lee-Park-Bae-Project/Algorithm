def solution(priorities, location):
    answer = 1
    printerVal = []
    for a in range(0, len(priorities)):
        printerVal.append(a)
    maxVal = max(priorities)
    subVal = priorities[location]
    while printerVal:
        temp = priorities.pop(0)
        temp2 = printerVal.pop(0)
        # print(temp,temp)
        if temp >= maxVal:
            if temp2 == location:
                break
            else:
                answer += 1
                maxVal = max(priorities)
        else:
            priorities.append(temp)
            printerVal.append(temp2)

    return answer
