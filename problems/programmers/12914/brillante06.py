def solution(n):
    answer = 0
    a, b = 1, 2
    if n == 1:
        return 1
    elif n == 2:
        return 2
    for i in range(3, n):
        temp = b
        b = a+b
        a = temp

    return (a+b) % 1234567
