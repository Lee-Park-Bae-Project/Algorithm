from collections import deque
s = int(input())

q = deque([(1, 0, 0)])
ans = 0
isVisit = set([1, 0])
while len(q) != 0:
    display, clipboard, cost = q.popleft()
    if display == s:
        ans = cost
        break
    if (display, display) not in isVisit:
        isVisit.add((display, display))
        q.append((display, display, cost+1))
    if clipboard != 0 and (display+clipboard, clipboard) not in isVisit:
        isVisit.add((display+clipboard, clipboard))
        q.append((display+clipboard, clipboard, cost+1))
    if display > 0 and (display-1, clipboard) not in isVisit:
        isVisit.add((display-1, clipboard))
        q.append((display-1, clipboard, cost+1))
print(ans)
