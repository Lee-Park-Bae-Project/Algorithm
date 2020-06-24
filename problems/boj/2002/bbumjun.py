n = int(input())
inTunnel = []
outTunnel = []
for i in range(n):
    inTunnel.append(input())
for i in range(n):
    outTunnel.append(input())
ans = 0
for i in range(n):
    car = outTunnel.pop(0)
    if inTunnel[0] == car:
        inTunnel.pop(0)
    else:
        ans += 1
        inTunnel.remove(car)
print(ans)
