from collections import defaultdict
n = int(input())
m = int(input())
lst = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
q, flag, wed = [(1, 0)], [False]*501, 0
flag[1] = True
while q:
    friend, rel = q.pop(0)
    if friend != 1 and rel <= 2:
        wed += 1
    for i in lst[friend]:
        if flag[i] is False:
            q.append((i, rel+1))
            flag[i] = True

print(wed)
