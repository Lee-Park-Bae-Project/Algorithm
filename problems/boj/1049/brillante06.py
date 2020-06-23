n, m = list(map(int, input().split()))
m1 = 100001
m2 = 100001
cnt = None
for i in range(m):
    res = list(map(int, input().split()))
    m1 = min(m1, res[0])
    m2 = min(m2, res[1])
if n < 6:
    res = min(m2*n, m1)
else:
    if m2*6 > m1:
        res = (n//6)*m1+min((n % 6)*m2, m1)
    else:
        res = n*m2
print(res)
