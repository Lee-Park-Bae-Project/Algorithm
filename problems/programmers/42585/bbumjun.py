def solution(arrangement):
    answer = 0
    stack = []
    i = 0
    while i < len(arrangement):
        if arrangement[i] == '(':
            if arrangement[i+1] == ')':
                answer += len(stack)
                i += 1
            else:
                stack.append(arrangement[i])
        else:
            answer += 1
            stack.pop()
        i += 1
    return answer
