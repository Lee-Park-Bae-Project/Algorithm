n = int(input())
boat = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
res = 0
if max(box) > max(boat):
    res = -1
else:
    box.sort(reverse=True)
    boat.sort(reverse=True)
    cnt = 0
    while cnt < m:
        start = 0
        for i in range(len(box)):
            if box[i] != -1 and boat[start] >= box[i]:
                start += 1
                box[i] = -1
                cnt += 1
            if start >= len(boat):
                break
        res += 1
print(res)
