from sys import stdin
import heapq
n, m = map(int, stdin.readline().split())
jewels = []
bags = []
for i in range(n):
    jewels.append(list(map(int, stdin.readline().split())))
for i in range(m):
    bags.append((int(stdin.readline())))
jewels.sort(key=lambda item: item[1], reverse=True)
for i in range(n):
    jewels[i].insert(0, i)  # 가격 순위 매김
jewels.sort(key=lambda item: item[1])  # 가벼운 기준으로 다시 정렬
bags.sort()
answer = 0
pq = []
idx = 0
for i in range(m):
    while idx < n and bags[i] >= jewels[idx][1]:
        heapq.heappush(pq, (jewels[idx][0], jewels[idx][2]))
        idx += 1
    if len(pq) != 0:
        answer += heapq.heappop(pq)[1]

print(answer)
