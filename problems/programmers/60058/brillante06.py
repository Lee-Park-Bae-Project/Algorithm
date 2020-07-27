def seperate(sen):
    left, right = 0, 0
    u, v, answer = '', '', ''
    makeR = []
    if sen == '':
        return ''
    for a in sen:
        if a == ')':
            right += 1
            if len(makeR) != 0:
                makeR.pop()
        elif a == '(':
            makeR.append(a)
            left += 1
        if right == left and right != 0:
            u = sen[:(right+left)]
            v = sen[(right+left):]
            break
    print(u, v)
    if len(makeR) == 0:
        u += seperate(v)
        return u
    else:
        temp = '('
        temp += seperate(v)
        temp += ')'
        u = u[1:len(u)-1]
        for i in range(0, len(u)):
            if u[i] == '(':
                temp += ')'
            elif u[i] == ')':
                temp += '('
        return temp


def solution(p):
    answer = seperate(p)
    return answer
