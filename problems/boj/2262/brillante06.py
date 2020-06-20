n = int(input())
tour = list(map(int, input().split()))
res = 0
while n != 1:
    k = tour.index(max(tour))
    if k > 0 and k < len(tour)-1:
        res += min(abs(tour[k]-tour[k+1]), abs(tour[k]-tour[k-1]))
        tour.remove(tour[k])
    else:
        if k == 0:
            res += abs(tour[k]-tour[k+1])
        if k == len(tour)-1:
            res += abs(tour[k]-tour[k-1])
        tour.remove(tour[k])
    n -= 1

print(res)
