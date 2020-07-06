n = int(input())
requests = list(map(int, input().split()))
budget = int(input())
ans = 0
if sum(requests) <= budget:
    print(max(requests))
else:
    minBudget = budget//n
    maxBudget = max(requests)
    while minBudget <= maxBudget:
        midBudget = (minBudget+maxBudget)//2
        total = 0
        maxB = 0
        for request in requests:
            b = midBudget if midBudget < request else request
            total += b
            if maxB < b:
                maxB = b
        if total <= budget:
            ans = maxB
            minBudget = midBudget + 1
        else:
            maxBudget = midBudget - 1
    print(ans)
