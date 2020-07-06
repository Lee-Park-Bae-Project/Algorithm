n = int(input())
money = list(map(int, input().split()))
m = int(input())

start, end, ans = 0, max(money), 0
while start <= end:
    mid = (start+end)//2
    total = 0
    for i in range(n):
        if mid < money[i]:
            total += mid
        else:
            total += money[i]
    if total <= m:
        if ans < mid:
            ans = mid
        start = mid+1
    else:
        end = mid-1
print(ans)
