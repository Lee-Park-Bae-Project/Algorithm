n, c = map(int, input().split())
lst, ans = [], 0
for i in range(n):
    lst.append(int(input()))
lst.sort()
start = lst[1]-lst[0]
end = lst[len(lst)-1]-lst[0]
while start <= end:
    first = lst[0]
    mid, temp = (start+end)//2, 1
    for i in range(1, n):
        if lst[i]-first >= mid:
            temp += 1
            first = lst[i]
    if temp >= c:
        ans = mid
        start = mid+1
    else:
        end = mid-1
print(ans)
