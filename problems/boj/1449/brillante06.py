from sys import stdin
# 1449
n, l = map(int, (input().split()))
cnt = 1
hole = list(map(int, input().split()))
hole.sort()
minVal = hole[0]
for i in range(1, n):
    if (hole[i]-minVal)+1 > l:
        minVal = hole[i]
        cnt += 1
print(cnt)
