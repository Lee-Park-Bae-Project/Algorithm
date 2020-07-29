def solution(p):

    answer = recursive(p)
    return answer


def splitStr(s):
    stack = []
    bal = 0
    i = 0
    while i < len(s):
        stack.append(s[i])
        if s[i] == '(':
            bal += 1
        else:
            bal -= 1
        if bal == 0:
            break
        i += 1
    return ''.join(stack), s[i+1:]


def flip(s):
    tempS = ''
    for i in range(1, len(s)-1):
        if s[i] == '(':
            tempS += ')'
        else:
            tempS += '('
    return tempS


def recursive(s):
    if s == '':
        return s
    u, v = splitStr(s)
    if u[0] == '(' and u[-1] == ')':
        result = u + recursive(v)
        return result
    else:
        tempS = '('+recursive(v)+')'
        result = tempS + flip(u)
        return result


print(solution("()))((()"))
