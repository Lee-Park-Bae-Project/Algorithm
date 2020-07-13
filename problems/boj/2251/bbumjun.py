from collections import deque
from copy import deepcopy


def moveWater(a, b):
    emptySpace = b[1] - b[0]
    if a[0] >= emptySpace:
        b[0] = b[1]
        a[0] -= emptySpace
    else:
        b[0] += a[0]
        a[0] = 0


a, b, c = map(int, input().split())
ans = []
isVisit = set([(0, 0, c)])
q = deque([([0, a], [0, b], [c, c])])
while len(q) != 0:
    bottles = q.popleft()
    if bottles[0][0] == 0:
        ans.append(bottles[2][0])
    for i in range(len(bottles)):
        for j in range(len(bottles)):
            if i == j or bottles[i][0] == 0:
                continue
            newBottles = deepcopy(bottles)
            moveWater(newBottles[i], newBottles[j])
            s = (newBottles[0][0], newBottles[1][0], newBottles[2][0])
            if s in isVisit:
                continue
            isVisit.add(s)
            q.append(deepcopy(newBottles))
print(' '.join(map(str, sorted(ans))))
