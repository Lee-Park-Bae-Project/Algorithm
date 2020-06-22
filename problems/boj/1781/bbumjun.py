from sys import stdin
import heapq
n = int(stdin.readline())
problems = []
for i in range(n):
    problems.append(list(map(int, stdin.readline().split())))

problems.sort(key=lambda problem: problem[1], reverse=True)
for i in range(n):
    problems[i].insert(0, i)
problems.sort(key=lambda problem: problem[1], reverse=True)
answer = 0
pq = []
idx = 0
for i in range(n, 0, -1):
    while idx < n and problems[idx][1] >= i:
        heapq.heappush(pq, problems[idx])
        idx += 1
    if len(pq) != 0:
        answer += heapq.heappop(pq)[2]
print(answer)
