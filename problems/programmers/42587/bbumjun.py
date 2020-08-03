from collections import deque


def solution(priorities, location):
    answer = 0
    dq = deque(map(lambda item: [item, False], priorities))
    dq[location][1] = True

    while True:
        maxN = max(dq)[0]
        head = dq.popleft()
        if head[0] == maxN:
            answer += 1
            if head[1] == True:
                break
        else:
            dq.append(head)

    return answer


print(solution([1, 1, 9, 1, 1, 1]	, 0))
