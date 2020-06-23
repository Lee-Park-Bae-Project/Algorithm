n = int(input())
nodes = list(map(int, input().split()))

answer = 0
while len(nodes) > 1:
    winners = []
    for i in range(len(nodes)-1):
        winners.append((min(nodes[i], nodes[i+1]), max(nodes[i], nodes[i+1])))
    winner, loser = max(winners)
    answer += abs(winner-loser)
    nodes.remove(loser)
print(answer)
