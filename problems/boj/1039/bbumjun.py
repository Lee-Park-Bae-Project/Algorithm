import queue
n, k = map(int, input().split())
n = list(str(n))
res = -1
q = queue.Queue()
q.put((n, 0))
isVisit = set([])
depth = 0

while q.empty() == False:
    num, cnt = q.get()
    if depth != cnt:
        isVisit = set([])
        depth = cnt
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            newNum = num[:]
            newNum[i], newNum[j] = newNum[j], newNum[i]
            numStr = ''.join(newNum)
            if numStr[0] == '0':
                continue
            if cnt == k-1:
                if res < int(numStr):
                    res = int(numStr)
            elif numStr not in isVisit:
                isVisit.add(numStr)
                q.put((newNum, cnt+1))
print(res)
