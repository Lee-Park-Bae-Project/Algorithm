from math import sqrt


def solution(brown, yellow):
    size = brown+yellow
    l, r = 3, sqrt(size)
    while l <= r:
        h = (l+r)//2
        w = size / h
        if w % 1 == 0 and (h-2) * (w-2) == yellow:
            return [int(w), int(h)]
        if (h-2) * (w-2) >= yellow:
            r = h-1
        else:
            l = h+1


print(solution(24, 24))
