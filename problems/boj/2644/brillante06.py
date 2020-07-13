from collections import defaultdict
n = int(input())
start, end = map(int, input().split())
m = int(input())
dic = defaultdict(list)
lst = set()
for _ in range(m):
    t1, t2 = map(int, input().split())
    dic[t1].append(t2)
    dic[t2].append(t1)


def bfs(a, b):
    flag, q = [False]*(n+1), [(a, 0)]
    while len(q) != 0:
        z, y = q.pop(0)
        if z == b:
            return y
        leng = len(dic[z])
        for i in dic[z]:
            if flag[i] == False:
                flag[i] = True
                q.append(tuple((i, y+1)))

    return -1


print(bfs(start, end))
