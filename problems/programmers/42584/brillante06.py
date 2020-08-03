def solution(prices):
    answer = []
    for i in range(len(prices)):
        pri = 0
        for j in range(i+1, len(prices)):
            pri += 1
            if prices[i] > prices[j]:
                break
        answer.append(pri)
    return answer
